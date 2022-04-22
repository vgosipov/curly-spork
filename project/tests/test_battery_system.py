import allure
import pytest

from project.support import constants
from project.support.constants import GearPosition, BatteryState, BrakePedalState, AccPedalPosState, ReqTorque
from project.utils.pin_factory import PinFactory
from project.utils.signal_factory import SignalFactory


class TestBatterySystem:
    @allure.title('28. Проверка системы при ошибке определения состояния батареи')
    @pytest.mark.parametrize('gear_1_voltage, gear_2_voltage, brake_pedal_voltage, acc_pedal_pos_voltage',
                             [(1.48, 2.28, 1.5, 1.5)])
    def test_scenario_28_battery_is_in_error(self, steps, gear_1_voltage, gear_2_voltage,
                                             brake_pedal_voltage, acc_pedal_pos_voltage):

        expected_gear_pos_sig = SignalFactory.gear_pos(value=GearPosition.NEUTRAL)
        expected_req_torque_sig = SignalFactory.req_torque(value=ReqTorque.Nm_0)
        expected_break_sig = SignalFactory.brake_pedal(value=BrakePedalState.ERROR)
        expected_acc_sig = SignalFactory.acc_pedal(value=AccPedalPosState.ERROR)

        expected_gear_1_pin = PinFactory.gear_1(voltage=constants.GEAR_1_PIN_ZERO_VOLTAGE)
        expected_gear_2_pin = PinFactory.gear_2(voltage=constants.GEAR_2_PIN_ZERO_VOLTAGE)
        expected_break_pin = PinFactory.brake_pedal(voltage=constants.BRAKE_PEDAL_PIN_ZERO_VOLTAGE)
        expected_acc_pin = PinFactory.acc_pedal(voltage=constants.ACC_PEDAL_PIN_ZERO_VOLTAGE)

        steps.battery.set_battery_state(BatteryState.ERROR)
        steps.vehicle_api.assert_signals((expected_gear_pos_sig, expected_req_torque_sig, expected_break_sig,
                                          expected_acc_sig))
        steps.vehicle_api.assert_pins((expected_gear_1_pin, expected_gear_2_pin, expected_break_pin, expected_acc_pin))

        gear_1_pin = PinFactory.gear_1(voltage=gear_1_voltage)
        gear_2_pin = PinFactory.gear_2(voltage=gear_2_voltage)
        brake_pedal_pin = PinFactory.brake_pedal(voltage=brake_pedal_voltage)
        acc_pedal_pin = PinFactory.acc_pedal(voltage=acc_pedal_pos_voltage)
        steps.vehicle_api.set_pins([gear_1_pin, gear_2_pin, brake_pedal_pin, acc_pedal_pin])
        steps.vehicle_api.assert_pins((expected_gear_1_pin, expected_gear_2_pin, expected_break_pin, expected_acc_pin))
