import re

import pytest
from mimesis import Person
from mimesis.data import BLOOD_GROUPS, GENDER_SYMBOLS
from mimesis.enums import Gender, TitleType
from mimesis.exceptions import NonEnumerableError

from . import patterns


class TestPerson(object):
    @pytest.fixture
    def _person(self):
        return Person()

    def test_str(self, person):
        assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(person))

    @pytest.mark.parametrize(
        "minimum, maximum",
        [
            (16, 18),
            (18, 21),
            (22, 28),
        ],
    )
    def test_age(self, _person, minimum, maximum):
        result = _person.age(minimum, maximum)
        assert (result >= minimum) and (result <= maximum)

    def test_age_store(self, _person):
        result = _person._store["age"]
        assert result == 0

    def test_age_update(self, _person):
        result = _person.age() - _person._store["age"]
        assert result == 0

    def test_work_experience(self, _person):
        result = _person.work_experience(working_start_age=0) - _person._store["age"]
        assert result == 0

    def test_work_experience_store(self, _person):
        result = _person.work_experience() - _person.work_experience()
        assert result == 0

    def test_work_experience_extreme(self, _person):
        result = _person.work_experience(working_start_age=100000)
        assert result == 0

    def test_password(self, _person):
        result = _person.password(length=15)
        assert len(result) == 15

        result = _person.password(hashed=True)
        assert len(result) == 32

    @pytest.mark.parametrize(
        "mask",
        [
            "C-d",
            "C.d",
            "C_d",
            "CC-d",
            "CC.d",
            "CC_d",
            "Cd",
            "l-d",
            "l.d",
            "l_d",
            "ld",
            None,
        ],
    )
    def test_username(self, _person, mask):
        template_patterns = {
            "C-d": r"^[A-Z][a-z]+-[0-9]+$",
            "C.d": r"^[A-Z][a-z]+\.[0-9]+$",
            "C_d": r"^[A-Z][a-z]+_[0-9]+$",
            "CC-d": r"^[A-Z][a-z]+[A-Z][a-z]+-[0-9]+$",
            "CC.d": r"^[A-Z][a-z]+[A-Z][a-z]+\.[0-9]+$",
            "CC_d": r"^[A-Z][a-z]+[A-Z][a-z]+_[0-9]+$",
            "Cd": r"^[A-Z][a-z]+[0-9]+$",
            "l-d": r"^[a-z]+-[0-9]+$",
            "l.d": r"^[a-z]+\.[0-9]+$",
            "l_d": r"^[a-z]+_[0-9]+$",
            "ld": r"^[a-z]+[0-9]+$",
            None: r"^[A-Za-z]{2,}[\.\-\_]?[0-9]+$",
        }

        result = _person.username(mask=mask)
        assert re.match(template_patterns[mask], result)

    def test_username_drange(self, _person):
        username = _person.username(mask="U.d", drange=(1000, 2000))
        username, digits = username.split(".")
        assert 1000 <= int(digits.strip()) <= 2000

        with pytest.raises(ValueError):
            _person.username(drange=(1000, 2000, 3000))  # type: ignore

    def test_username_unsupported_mask(self, _person):
        with pytest.raises(ValueError):
            _person.username(mask="cda")

    @pytest.mark.parametrize(
        "unique",
        [
            False,
            True,
        ],
    )
    def test_email(self, _person, unique):
        result = _person.email()
        assert re.match(patterns.EMAIL_REGEX, result)

        domains = ["@example.com", "example.com"]
        result = _person.email(domains=domains)
        assert re.match(patterns.EMAIL_REGEX, result)
        assert result.split("@")[1] == "example.com"

        if unique:
            count = 1000000
            generated = set()

            for i in range(count):
                email = _person.email(
                    domains=["example.com"],
                    unique=unique,
                )
                email_username = email.split("@")[0].strip()
                generated.add(email_username)

            assert len(generated) == count

    def test_height(self, _person):
        result = _person.height(minimum=1.60, maximum=1.90)
        assert result.startswith("1")
        assert isinstance(result, str)

    def test_weight(self, _person):
        result = _person.weight(minimum=40, maximum=60)
        assert result >= 40
        assert result <= 60

    def test_blood_type(self, _person):
        result = _person.blood_type()
        assert result in BLOOD_GROUPS

    def test_identifier(self, _person):
        result = _person.identifier()
        mask = "##-##/##"
        assert len(mask) == len(result)

        result = _person.identifier(mask="##-##/## @@")
        suffix = result.split(" ")[1]
        assert suffix.isalpha()

    @pytest.mark.parametrize(
        "gender",
        [
            Gender.FEMALE,
            Gender.MALE,
        ],
    )
    def test_name(self, person, gender):
        result = person.name(gender=gender)
        assert result in person._data["names"][gender.value]

    @pytest.mark.parametrize(
        "gender",
        [
            Gender.FEMALE,
            Gender.MALE,
        ],
    )
    def test_first_name(self, person, gender):
        result = person.first_name(gender=gender)
        assert result in person._data["names"][gender.value]

    def test_name_with_none(self, _person):
        result = _person.name(gender=None)
        names = _person._data["names"]

        females = names["female"]
        males = names["male"]
        assert result is not None
        assert (result in females) or (result in males)

    def test_name_unexpected_gender(self, person):
        with pytest.raises(NonEnumerableError):
            person.name(gender="nil")

    def test_telephone(self, person):
        result = person.telephone()
        assert result is not None

        mask = "+5 (###)-###-##-##"
        result = person.telephone(mask=mask)
        head = result.split(" ")[0]
        assert head == "+5"

    @pytest.mark.parametrize(
        "gender",
        [
            Gender.FEMALE,
            Gender.MALE,
        ],
    )
    def test_surname(self, person, gender):
        surnames = person._data["surnames"]

        # Surnames separated by gender.
        if isinstance(surnames, dict):
            result = person.surname(gender=gender)
            assert result in surnames[gender.value]
        else:
            result = person.surname()
            assert result in surnames
            result = person.last_name()
            assert result in surnames

    @pytest.mark.parametrize(
        "gender",
        [
            Gender.FEMALE,
            Gender.MALE,
        ],
    )
    def test_full_name(self, person, gender):
        result = person.full_name(gender=gender)

        result = result.split(" ")
        assert result[0] is not None
        assert result[1] is not None

        result = person.full_name(reverse=True)
        assert result is not None

        with pytest.raises(NonEnumerableError):
            person.full_name(gender="nil")

    def test_gender(self, person):
        result = person.gender()
        assert result in person._data["gender"]

        result = person.gender(symbol=True)
        assert result in GENDER_SYMBOLS

        # The four codes specified in ISO/IEC 5218 are:
        # 0 = not known, 1 = male, 2 = female, 9 = not applicable.
        codes = [0, 1, 2, 9]
        iso5218 = person.gender(iso5218=True)
        assert iso5218 in codes

    def test_sex(self, person):
        result = person.sex()
        assert result in person._data["gender"]

        result = person.gender(symbol=True)
        assert result in GENDER_SYMBOLS

        # The four codes specified in ISO/IEC 5218 are:
        # 0 = not known, 1 = male, 2 = female, 9 = not applicable.
        codes = [0, 1, 2, 9]
        iso5218 = person.gender(iso5218=True)
        assert iso5218 in codes

    def test_profession(self, person):
        result = person.occupation()
        assert result in person._data["occupation"]

    def test_university(self, person):
        result = person.university()
        assert result in person._data["university"]

    def test_academic_degree(self, person):
        result = person.academic_degree()
        assert result in person._data["academic_degree"]

    def test_language(self, person):
        result = person.language()
        assert result in person._data["language"]

    def test_worldview(self, person):
        result = person.worldview()
        assert result in person._data["worldview"]

    def test_views_on(self, person):
        result = person.views_on()
        assert result in person._data["views_on"]

    def test_political_views(self, person):
        result = person.political_views()
        assert result in person._data["political_views"]

    @pytest.mark.parametrize(
        "title_type",
        [
            TitleType.ACADEMIC,
            TitleType.TYPICAL,
            None,
        ],
    )
    @pytest.mark.parametrize(
        "gender",
        [
            Gender.FEMALE,
            Gender.MALE,
            None,
        ],
    )
    def test_title(self, person, gender, title_type):
        result = person.title(gender=gender, title_type=title_type)
        assert result is not None

        with pytest.raises(NonEnumerableError):
            person.title(title_type="nil")
            person.title(gender="nil")

    @pytest.mark.parametrize(
        "gender",
        [
            Gender.FEMALE,
            Gender.MALE,
        ],
    )
    def test_nationality(self, person, gender):
        nationality = person._data["nationality"]
        if isinstance(nationality, dict):
            result = person.nationality(gender=gender)
            assert result in person._data["nationality"][gender.value]

        result = person.nationality()
        assert result is not None


class TestSeededPerson(object):
    @pytest.fixture
    def p1(self, seed):
        return Person(seed=seed)

    @pytest.fixture
    def p2(self, seed):
        return Person(seed=seed)

    def test_age(self, p1, p2):
        assert p1.age() == p2.age()
        assert p1.age(12, 42) == p2.age(12, 42)

    def test_work_experience(self, p1, p2):
        assert p1.work_experience() == p2.work_experience()
        assert p1.work_experience(19) == p2.work_experience(19)

    def test_password(self, p1, p2):
        assert p1.password() == p2.password()
        assert p1.password(length=12, hashed=True) == p2.password(
            length=12, hashed=True
        )

    def test_username(self, p1, p2):
        assert p1.username() == p2.username()
        assert p1.username(mask="l_d") == p2.username(mask="l_d")

    def test_email(self, p1, p2):
        assert p1.email() == p2.email()
        assert p1.email(domains=["@mimesis.io"]) == p2.email(domains=["@mimesis.io"])

        with pytest.raises(ValueError):
            p1.email(unique=True)

    def test_height(self, p1, p2):
        assert p1.height() == p2.height()
        assert p1.height(1.7, 2.1) == p2.height(1.7, 2.1)

    def test_weight(self, p1, p2):
        assert p1.weight() == p2.weight()
        assert p1.weight(16, 42) == p2.weight(16, 42)

    def test_blood_type(self, p1, p2):
        assert p1.blood_type() == p2.blood_type()

    def test_identifier(self, p1, p2):
        assert p1.identifier() == p2.identifier()
        assert p1.identifier(mask="##") == p2.identifier(mask="##")

    def test_name(self, p1, p2):
        assert p1.name() == p2.name()
        assert p1.name(gender=Gender.FEMALE) == p2.name(gender=Gender.FEMALE)

    def test_first_name(self, p1, p2):
        assert p1.first_name() == p2.first_name()
        assert p1.first_name(gender=Gender.FEMALE) == p2.first_name(
            gender=Gender.FEMALE
        )

    def test_telephone(self, p1, p2):
        assert p1.telephone() == p2.telephone()
        assert p1.telephone(mask="(x)-xx-xxx", placeholder="x") == p2.telephone(
            mask="(x)-xx-xxx", placeholder="x"
        )

    def test_surname(self, p1, p2):
        assert p1.surname() == p2.surname()
        assert p1.last_name(gender=Gender.MALE) == p2.last_name(gender=Gender.MALE)

    def test_full_name(self, p1, p2):
        assert p1.full_name() == p2.full_name()
        assert p1.full_name(gender=Gender.FEMALE, reverse=True) == p2.full_name(
            gender=Gender.FEMALE, reverse=True
        )

    def test_gender(self, p1, p2):
        assert p1.gender() == p2.gender()
        assert p1.gender(iso5218=True, symbol=True) == p2.gender(
            iso5218=True, symbol=True
        )

    def test_sex(self, p1, p2):
        assert p1.sex() == p2.sex()
        assert p1.sex(iso5218=True, symbol=True) == p2.sex(iso5218=True, symbol=True)

    def test_occupation(self, p1, p2):
        assert p1.occupation() == p2.occupation()

    def test_university(self, p1, p2):
        assert p1.university() == p2.university()

    def test_academic_degree(self, p1, p2):
        assert p1.academic_degree() == p2.academic_degree()

    def test_language(self, p1, p2):
        assert p1.language() == p2.language()

    def test_worldview(self, p1, p2):
        assert p1.worldview() == p2.worldview()

    def test_views_on(self, p1, p2):
        assert p1.views_on() == p2.views_on()

    def test_political_views(self, p1, p2):
        assert p1.political_views() == p2.political_views()

    def test_title(self, p1, p2):
        assert p1.title() == p2.title()
        assert p1.title(gender=Gender.FEMALE, title_type=TitleType.TYPICAL) == p2.title(
            gender=Gender.FEMALE, title_type=TitleType.TYPICAL
        )

    def test_nationality(self, p1, p2):
        assert p1.nationality() == p2.nationality()
        assert p1.nationality(Gender.FEMALE) == p2.nationality(Gender.FEMALE)
