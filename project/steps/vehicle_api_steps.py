from typing import Sequence

import allure
from hamcrest import assert_that

from project.api import VehicleApi
from project.models.pin import Pin
from project.models.signal import Signal
from framework.utils import soft_assertions
from framework.utils.custom_assertions import dataclass_equals


class VehicleApiSteps:
    def __init__(self, api: VehicleApi):
        self.api = api

    @allure.step('Set pin: {pin}')
    def set_pin(self, pin: Pin) -> None:
        self.api.update_pin(pin.pin_id, pin.voltage)

    @allure.step('Set pins')
    def set_pins(self, pins: Sequence[Pin]) -> None:
        self.api.update_pins(*pins)

    @allure.step('Assert signal')
    def assert_signal(self, signal: Signal) -> None:
        actual = self.api.get_signal(signal.sig_id)
        assert_that(actual, dataclass_equals(signal), f'Signal "{actual.name}" is incorrect')

    @allure.step('Assert signals')
    def assert_signals(self, signals: Sequence[Signal]) -> None:
        actual_signals = self.api.get_signals()
        assertions = [(signal in actual_signals, f'Following "{signal.name}" signal is not found in signals: {signal}')
                      for signal
                      in signals]
        soft_assertions.collect_multiple(*assertions)

    @allure.step('Assert pins')
    def assert_pins(self, pins: Sequence[Pin]) -> None:
        actual_pins = self.api.get_pins()
        assertions = [(pin in actual_pins, f'Following "{pin.name}" pin is not found in pins: {pin}')
                      for pin
                      in pins]
        soft_assertions.collect_multiple(*assertions)

