from framework.utils.logger import Logger
from framework.utils import AllureLogger


def pytest_runtestloop(session) -> None:
    allure_logger = AllureLogger()
    Logger().info('Adding Allure logger')
    Logger().add_handler(allure_logger)


pytest_plugins = [
    "project.tests.fixtures.setup_tests"
]
