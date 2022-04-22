import allure
from hamcrest import assert_that

from project.api import VehicleApi
from project.support import test_data
from project.support import constants
from framework.utils.custom_assertions import dataclass_equals
from project.utils.pin_factory import PinFactory
from project.utils.signal_factory import SignalFactory


class BatterySteps:
    def __init__(self, api: VehicleApi, pin_factory: PinFactory, signal_factory: SignalFactory):
        self.api = api
        self.pin_factory = pin_factory
        self.signal_factory = signal_factory

    @allure.step('Set BatteryState: "{battery_state}"')
    def set_battery_state(self, battery_state: str) -> None:
        battery_pin = test_data.BATTERY_PIN[battery_state]
        self.api.update_pin(battery_pin.pin_id, battery_pin.voltage)

    @allure.step('Assert BatteryState')
    def assert_gear_pos_signal(self, expected_state: str) -> None:
        expected = self.signal_factory.battery_state(value=expected_state)
        actual = self.api.get_signal(constants.BATTERY_SIG_NAME)
        assert_that(actual, dataclass_equals(expected), f'Signal "{expected.name}" is incorrect')
