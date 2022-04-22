from typing import Union

import allure
from hamcrest import assert_that

from project.api import VehicleApi
from project.support import test_data
from project.support import constants
from framework.utils.custom_assertions import dataclass_equals
from project.utils.pin_factory import PinFactory
from project.utils.signal_factory import SignalFactory


class BrakePedalSteps:
    def __init__(self, api: VehicleApi, pin_factory: PinFactory, signal_factory: SignalFactory):
        self.api = api
        self.pin_factory = pin_factory
        self.signal_factory = signal_factory

    @allure.step('Set BrakePedal pin voltage: {voltage}')
    def set_brake_pedal_pin(self, voltage: Union[int, float]) -> None:
        self.api.update_pin(constants.BRAKE_PEDAL_PIN_ID, voltage)

    @allure.step('Set BrakePedal state: {state}')
    def set_brake_pedal_state(self, state: str) -> None:
        pin = test_data.BRAKE_PEDAL_PIN[state]
        self.api.update_pin(pin.pin_id, pin.voltage)

    @allure.step('Assert BrakePedal pin')
    def assert_brake_pedal_pin(self, voltage: Union[int, float]) -> None:
        pin = self.pin_factory.brake_pedal(voltage=voltage)
        actual = self.api.get_pin(pin.pin_id)
        assert_that(actual, dataclass_equals(pin), f'Pin "{pin.name}" is incorrect')

    @allure.step('Assert BrakePedal signal')
    def assert_brake_pedal_signal(self, expected_brake_pedal_pos: str) -> None:
        signal = self.signal_factory.brake_pedal(value=expected_brake_pedal_pos)
        actual = self.api.get_signal(signal.sig_id)
        assert_that(actual, dataclass_equals(signal), f'Signal "{signal.name}" is incorrect')
