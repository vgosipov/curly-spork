from typing import Union

import allure
from hamcrest import assert_that

from project.api import VehicleApi
from project.support import test_data
from project.support import constants
from framework.utils.custom_assertions import dataclass_equals
from project.utils.pin_factory import PinFactory
from project.utils.signal_factory import SignalFactory


class AccelerationPedalSteps:
    def __init__(self, api: VehicleApi, pin_factory: PinFactory, signal_factory: SignalFactory):
        self.api = api
        self.pin_factory = pin_factory
        self.signal_factory = signal_factory

    @allure.step('Set AcceleratePedal pin voltage: {voltage}')
    def set_acc_pedal_pin(self, voltage: Union[int, float]) -> None:
        self.api.update_pin(constants.ACC_PEDAL_PIN_ID, voltage)

    @allure.step('Set AcceleratePedal position: {position}')
    def set_acc_pedal_pos(self, position: str) -> None:
        pin = test_data.ACC_PEDAL_PIN[position]
        self.api.update_pin(pin.pin_id, pin.voltage)

    @allure.step('Assert AcceleratePedal pin')
    def assert_acc_pedal_pin(self, voltage: Union[int, float]) -> None:
        pin = self.pin_factory.acc_pedal(voltage=voltage)
        actual = self.api.get_pin(pin.pin_id)
        assert_that(actual, dataclass_equals(pin), f'Pin "{pin.name}" is incorrect')

    @allure.step('Assert AcceleratePedal signal')
    def assert_acc_pedal_signal(self, expected_acc_pedal_pos: str) -> None:
        signal = self.signal_factory.acc_pedal(value=expected_acc_pedal_pos)
        actual = self.api.get_signal(signal.sig_id)
        assert_that(actual, dataclass_equals(signal), f'Signal "{signal.name}" is incorrect')

    @allure.step('Assert ReqTorque signal')
    def assert_req_torque_signal(self, expected_req_torque: str) -> None:
        signal = self.signal_factory.req_torque(value=expected_req_torque)
        actual = self.api.get_signal(signal.sig_id)
        assert_that(actual, dataclass_equals(signal), f'Signal "{signal.name}" is incorrect')
