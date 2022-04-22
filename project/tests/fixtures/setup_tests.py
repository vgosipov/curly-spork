import pytest

import config
from project.api import VehicleApi
from project.support import pytest_constants
from project.utils.pin_factory import PinFactory
from project.utils.signal_factory import SignalFactory
from project.utils.steps_factory import StepsFactory


def pytest_addoption(parser) -> None:
    parser.addoption(pytest_constants.BASE_URL_OPTION_NAME, action='store', default=config.BASE_URL)


@pytest.fixture(scope='session')
def api_object(request) -> VehicleApi:
    base_url = request.config.getoption(pytest_constants.BASE_URL_OPTION_NAME)
    return VehicleApi(base_url)


@pytest.fixture
def steps(api_object) -> StepsFactory:
    return StepsFactory(api_object, PinFactory(), SignalFactory())
