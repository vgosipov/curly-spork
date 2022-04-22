import allure

from framework.utils import soft_assertions
from project.api import VehicleApi
from project.models.vehicle_state import VehicleState
from project.support import test_data
from project.support.constants import AccPedalPosState, BrakePedalState, BatteryState, GearPosition
from project.utils.signal_factory import SignalFactory


class VehicleStateSteps:
    def __init__(self, api: VehicleApi, signal_factory: SignalFactory):
        self.api = api
        self.signal_factory = signal_factory

    @allure.step('Vehicle is in Drive')
    def vehicle_is_in_drive(self) -> None:
        battery_pin = test_data.BATTERY_PIN[BatteryState.READY]
        break_pin = test_data.BRAKE_PEDAL_PIN[BrakePedalState.PRESSED]
        acc_pin = test_data.ACC_PEDAL_PIN[AccPedalPosState.PERCENT_0]
        gear_1_pin, gear_2_pin = test_data.GEAR_PINS[GearPosition.DRIVE]
        self.api.update_pins(battery_pin, break_pin, acc_pin, gear_1_pin, gear_2_pin)

        break_pin = test_data.BRAKE_PEDAL_PIN[BrakePedalState.RELEASED]
        acc_pin = test_data.ACC_PEDAL_PIN[AccPedalPosState.PERCENT_30]
        self.api.update_pins(break_pin, acc_pin)

    @allure.step('Set Vehicle state to: {vehicle_state}')
    def set_vehicle_state(self, vehicle_state: VehicleState) -> None:
        battery_pin = test_data.BATTERY_PIN[vehicle_state.battery] \
            if vehicle_state.battery is not None else None
        break_pin = test_data.BRAKE_PEDAL_PIN[vehicle_state.brake_pedal] \
            if vehicle_state.brake_pedal is not None else None
        acc_pin = test_data.ACC_PEDAL_PIN[vehicle_state.acc_pedal] \
            if vehicle_state.acc_pedal is not None else None
        gear_1_pin, gear_2_pin = test_data.GEAR_PINS[vehicle_state.gear_pos] \
            if vehicle_state.gear_pos is not None else (None, None)
        pins = (pin for pin in (battery_pin, break_pin, acc_pin, gear_1_pin, gear_2_pin) if pin is not None)
        self.api.update_pins(*pins)

    @allure.step('Release acceleration pedal, press break pedal and set gear to: {gear}')
    def set_vehicle_gear(self, gear: str) -> None:
        break_pin = test_data.BRAKE_PEDAL_PIN[BrakePedalState.PRESSED]
        acc_pin = test_data.ACC_PEDAL_PIN[AccPedalPosState.PERCENT_0]
        gear_1_pin, gear_2_pin = test_data.GEAR_PINS[gear]
        self.api.update_pins(break_pin, acc_pin, gear_1_pin, gear_2_pin)

    @allure.step('Assert vehicle state')
    def assert_vehicle_state(self, vehicle_state: VehicleState) -> None:
        battery_signal = self.signal_factory.battery_state(value=vehicle_state.battery) \
            if vehicle_state.battery is not None else None
        break_signal = self.signal_factory.brake_pedal(value=vehicle_state.brake_pedal) \
            if vehicle_state.brake_pedal is not None else None
        acc_signal = self.signal_factory.acc_pedal(value=vehicle_state.acc_pedal) \
            if vehicle_state.acc_pedal is not None else None
        gear_signal = self.signal_factory.gear_pos(value=vehicle_state.gear_pos) \
            if vehicle_state.gear_pos is not None else None
        torque_signal = self.signal_factory.req_torque(value=vehicle_state.req_torque)\
            if vehicle_state.req_torque is not None else None

        signals = [battery_signal, break_signal, acc_signal, gear_signal, torque_signal]
        expected_signals = [signal for signal in signals if signal is not None]
        actual_signals = self.api.get_signals()

        assertions = [(signal in actual_signals, f'Following "{signal.name}" signal is not found in signals: {signal}')
                      for signal
                      in expected_signals]
        soft_assertions.collect_multiple(*assertions)
