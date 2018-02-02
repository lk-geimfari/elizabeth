"""Specific data provider for Russia (ru)."""

from typing import Optional

from mimesis.builtins.base import BaseSpecProvider
from mimesis.enums import Gender
from mimesis.utils import pull

__all__ = ['RussiaSpecProvider']


class RussiaSpecProvider(BaseSpecProvider):
    """Class that provides special data for Russia (ru)."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes."""
        super().__init__(*args, **kwargs)
        self._data = pull('builtin.json', 'ru')

    class Meta:
        """The name of the provider."""

        name = 'russia_provider'

    def generate_sentence(self) -> str:
        """Generate sentence from the parts.

        :return: Sentence.
        """
        sentences = self._data['sentence']
        sentence = [
            self.random.choice(sentences[k]) for k
            in ('head', 'p1', 'p2', 'tail')
        ]
        return '{0} {1} {2} {3}'.format(*sentence)

    def patronymic(self, gender: Optional[Gender] = None) -> str:
        """Generate random patronymic name.

        :param gender: Gender of person.
        :return: Patronymic name.

        :Example:
            Алексеевна.
        """
        gender = self._validate_enum(gender, Gender)
        patronymics = self._data['patronymic'][gender]
        return self.random.choice(patronymics)

    def passport_series(self, year: int = None) -> str:
        """Generate random series of passport.

        :param year: Year of manufacture.
        :type year: int or None
        :return: Series.

        :Example:
            02 15.
        """
        if not year:
            year = self.random.randint(10, 18)

        region = self.random.randint(1, 99)
        return '{:02d} {}'.format(region, year)

    def passport_number(self) -> int:
        """Generate random passport number.

        :return: Number.

        :Example:
            560430
        """
        return self.random.randint(
            100000, 999999)

    def series_and_number(self) -> str:
        """Generate a random passport number and series.

        :return: Series and number.

        :Example:
            57 16 805199.
        """
        return '{}{}'.format(
            self.passport_series(),
            self.passport_number(),
        )

    def snils(self) -> str:
        """Generate invalid ``SNILS``.

        This method does not generate SNILS using algorithm and
        it's mean that SNILS generated by this method can be invalid.

        :return: SNILS.

        :Example:
            451-952-540-41.
        """
        mask = '###-###-###-##'
        return self.random.custom_code(mask=mask)

    def inn(self) -> str:
        """Generate random, but valid ``INN``.

        :return: INN.
        """
        def control_sum(nums: list, t: str) -> int:
            digits = {
                'n2': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
                'n1': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            }
            number = 0
            length = digits[t]
            for i in range(0, len(length)):
                number += nums[i] * length[i]
            return number % 11 % 10

        numbers = []
        for x in range(0, 10):
            numbers.append(self.random.randint(1 if x == 0 else 0, 9))

        n2 = control_sum(numbers, 'n2')
        numbers.append(n2)
        n1 = control_sum(numbers, 'n1')
        numbers.append(n1)
        return ''.join([str(x) for x in numbers])

    def ogrn(self) -> str:
        """Generate random valid ``OGRN``.

        :return: OGRN.

        :Example:
            4715113303725.
        """
        numbers = []
        for _ in range(0, 12):
            numbers.append(self.random.randint(1 if _ == 0 else 0, 9))

        ogrn = ''.join([str(x) for x in numbers])
        check_sum = str(int(ogrn) % 11 % 10)

        return '{}{}'.format(ogrn, check_sum)

    def bic(self) -> str:
        """Generate random ``BIC`` (Bank ID Code).

        :return: BIC.

        :Example:
            044025575.
        """
        country_code = '04'
        code = '{:02}'.format(self.random.randint(1, 10))
        bank_number = '{:02}'.format(self.random.randint(0, 99))
        bank_office = '{:03}'.format(self.random.randint(50, 999))
        bic = country_code + code + bank_number + bank_office
        return bic
