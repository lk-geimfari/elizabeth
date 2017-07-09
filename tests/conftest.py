import elizabeth
from elizabeth.settings import SUPPORTED_LOCALES

import pytest

locales = list(SUPPORTED_LOCALES.keys())


@pytest.fixture(params=locales)
def generic(request):
    return elizabeth.Generic(request.param)


@pytest.fixture(params=locales)
def address(request):
    return elizabeth.Address(request.param)


@pytest.fixture(params=locales)
def business(request):
    return elizabeth.Business(request.param)


@pytest.fixture(params=locales)
def code(request):
    return elizabeth.Code(request.param)


@pytest.fixture(params=locales)
def dt(request):
    return elizabeth.Datetime(request.param)


@pytest.fixture(params=locales)
def food(request):
    return elizabeth.Food(request.param)


@pytest.fixture(params=locales)
def medicine(request):
    return elizabeth.Medicine(request.param)


@pytest.fixture(params=locales)
def personal(request):
    return elizabeth.Personal(request.param)


@pytest.fixture(params=locales)
def science(request):
    return elizabeth.Science(request.param)


@pytest.fixture(params=locales)
def structured(request):
    return elizabeth.Structured(request.param)


@pytest.fixture(params=locales)
def text(request):
    return elizabeth.Text(request.param)


@pytest.fixture()
def transport():
    return elizabeth.Transport()
