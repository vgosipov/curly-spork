import allure
import pytest

from project.models.vehicle_state import VehicleState
from project.support.constants import BatteryState, BrakePedalState, GearPosition, AccPedalPosState, ReqTorque


class TestAccelerationPedalSystem:
    @allure.title('1. Система положения педали акселератора реагирует корректно '
                  'на изменение напряжения при достаточном напряжении на батарее')
    @pytest.mark.parametrize('voltage,expected_acc_pos', [(0, 'Error'), (0.99, 'Error'), (1, '0 %'),
                                                          (1.01, '0 %'), (1.5, '0 %'), (1.99, '0 %'),
                                                          (2, '30 %'), (2.01, '30 %'), (2.2, '30 %'),
                                                          (2.49, '30 %'), (2.5, '50 %'), (2.51, '50 %'),
                                                          (2.7, '50 %'), (2.99, '50 %'), (3, '100 %'),
                                                          (3.01, '100 %'), (3.2, '100 %'), (3.49, '100 %'),
                                                          (3.5, 'Error'), (3.6, 'Error'), (4, 'Error')])
    def test_scenario_1_acc_pos_reacts_on_voltage_change(self, steps, voltage, expected_acc_pos):
        steps.vehicle_state.set_vehicle_state(VehicleState(battery=BatteryState.READY,
                                                           brake_pedal=BrakePedalState.RELEASED))
        steps.acceleration_pedal.set_acc_pedal_pin(voltage)
        steps.acceleration_pedal.assert_acc_pedal_signal(expected_acc_pos)

    @allure.title('3. Крутящий момент при нажатии на педаль акселератора при включенной передаче Drive '
                  'и при достаточном напряжении на батарее')
    @pytest.mark.parametrize('acc_pedal_pos,expected_req_torque', [(AccPedalPosState.PERCENT_30, ReqTorque.Nm_3000),
                                                                   (AccPedalPosState.PERCENT_50, ReqTorque.Nm_5000),
                                                                   (AccPedalPosState.PERCENT_100, ReqTorque.Nm_10000)])
    def test_scenario_3_req_torque_with_gear_in_drive(self, steps, acc_pedal_pos, expected_req_torque):
        steps.vehicle_state.set_vehicle_state(VehicleState(battery=BatteryState.READY))
        steps.vehicle_state.set_vehicle_gear(GearPosition.DRIVE)
        steps.vehicle_state.set_vehicle_state(VehicleState(brake_pedal=BrakePedalState.RELEASED))

        steps.acceleration_pedal.set_acc_pedal_pos(acc_pedal_pos)
        steps.acceleration_pedal.assert_req_torque_signal(expected_req_torque)

    @allure.title('10. Крутящий момент при одновременном нажатии на педаль акселератора и тормоза, '
                  'и при достаточном напряжении батареи')
    @pytest.mark.parametrize('acc_pedal_pos', (AccPedalPosState.PERCENT_30,
                                               AccPedalPosState.PERCENT_50,
                                               AccPedalPosState.PERCENT_100))
    @pytest.mark.parametrize('gear', (GearPosition.PARK, GearPosition.DRIVE,
                                      GearPosition.NEUTRAL, GearPosition.REVERSE))
    def test_scenario_10_req_torque_with_pressed_break_pedal(self, steps, acc_pedal_pos, gear):
        steps.vehicle_state.set_vehicle_state(VehicleState(battery=BatteryState.READY))
        steps.vehicle_state.set_vehicle_gear(gear)
        steps.vehicle_state.set_vehicle_state(VehicleState(brake_pedal=BrakePedalState.PRESSED,
                                                           acc_pedal=acc_pedal_pos))
        steps.acceleration_pedal.assert_req_torque_signal(ReqTorque.Nm_0)
