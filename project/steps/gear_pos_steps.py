from typing import Union

import allure
from hamcrest import assert_that

from project.api import VehicleApi
from project.support import test_data
from project.support import constants
from framework.utils.custom_assertions import dataclass_equals
from project.utils.pin_factory import PinFactory
from project.utils.signal_factory import SignalFactory


class GearPosSteps:
    def __init__(self, api: VehicleApi, pin_factory: PinFactory, signal_factory: SignalFactory):
        self.api = api
        self.pin_factory = pin_factory
        self.signal_factory = signal_factory

    @allure.step('Set Gear_1 pin voltage: {voltage}')
    def set_gear_1_pin(self, voltage: Union[int, float]) -> None:
        self.api.update_pin(constants.GEAR_1_PIN_ID, voltage)

    @allure.step('Set Gear_2 pin voltage: {voltage}')
    def set_gear_2_pin(self, voltage: Union[int, float]) -> None:
        self.api.update_pin(constants.GEAR_2_PIN_ID, voltage)

    @allure.step('Set GearPos to: "{gear}"')
    def set_gear(self, gear: str) -> None:
        gear_1_pin, gear_2_pin = test_data.GEAR_PINS[gear]
        self.api.update_pins(gear_1_pin, gear_2_pin)

    @allure.step('Assert GearPos signal')
    def assert_gear_pos_signal(self, expected_gear: str) -> None:
        expected = self.signal_factory.gear_pos(value=expected_gear)
        actual = self.api.get_signal(constants.GEAR_POS_SIG_ID)
        assert_that(actual, dataclass_equals(expected), f'Signal "{expected.name}" is incorrect')
