import allure
import pytest

from project.models.vehicle_state import VehicleState

from project.support.constants import GearPosition, BatteryState, BrakePedalState, AccPedalPosState, ReqTorque


class TestScenario30And31:
    @allure.title('{scenario}. Остановка (переключение передачи в {gear})')
    @pytest.mark.parametrize('scenario, gear', (('31', GearPosition.PARK), ('30', GearPosition.NEUTRAL)))
    def test_scenario_30_31(self, steps, scenario, gear):
        steps.vehicle_state.vehicle_is_in_drive()
        steps.acceleration_pedal.set_acc_pedal_pos(AccPedalPosState.PERCENT_0)
        steps.vehicle_state.assert_vehicle_state(VehicleState(brake_pedal=BrakePedalState.RELEASED,
                                                              acc_pedal=AccPedalPosState.PERCENT_0,
                                                              req_torque=ReqTorque.Nm_0,
                                                              gear_pos=GearPosition.DRIVE,
                                                              battery=BatteryState.READY))
        steps.brake_pedal.set_brake_pedal_state(BrakePedalState.PRESSED)
        steps.vehicle_state.assert_vehicle_state(VehicleState(brake_pedal=BrakePedalState.PRESSED,
                                                              acc_pedal=AccPedalPosState.PERCENT_0,
                                                              req_torque=ReqTorque.Nm_0,
                                                              gear_pos=GearPosition.DRIVE,
                                                              battery=BatteryState.READY))
        steps.gear_pos.set_gear(gear)
        steps.vehicle_state.assert_vehicle_state(VehicleState(brake_pedal=BrakePedalState.PRESSED,
                                                              acc_pedal=AccPedalPosState.PERCENT_0,
                                                              req_torque=ReqTorque.Nm_0,
                                                              gear_pos=gear,
                                                              battery=BatteryState.READY))
        steps.brake_pedal.set_brake_pedal_state(BrakePedalState.RELEASED)
        steps.vehicle_state.assert_vehicle_state(VehicleState(brake_pedal=BrakePedalState.RELEASED,
                                                              acc_pedal=AccPedalPosState.PERCENT_0,
                                                              req_torque=ReqTorque.Nm_0,
                                                              gear_pos=gear,
                                                              battery=BatteryState.READY))
        steps.brake_pedal.set_brake_pedal_state(BrakePedalState.PRESSED)
        steps.vehicle_state.assert_vehicle_state(VehicleState(brake_pedal=BrakePedalState.PRESSED,
                                                              acc_pedal=AccPedalPosState.PERCENT_0,
                                                              req_torque=ReqTorque.Nm_0,
                                                              gear_pos=gear,
                                                              battery=BatteryState.READY))
        steps.gear_pos.set_gear(GearPosition.DRIVE)
        steps.vehicle_state.assert_vehicle_state(VehicleState(brake_pedal=BrakePedalState.PRESSED,
                                                              acc_pedal=AccPedalPosState.PERCENT_0,
                                                              req_torque=ReqTorque.Nm_0,
                                                              gear_pos=GearPosition.DRIVE,
                                                              battery=BatteryState.READY))
        steps.brake_pedal.set_brake_pedal_state(BrakePedalState.RELEASED)
        steps.vehicle_state.assert_vehicle_state(VehicleState(brake_pedal=BrakePedalState.RELEASED,
                                                              acc_pedal=AccPedalPosState.PERCENT_0,
                                                              req_torque=ReqTorque.Nm_0,
                                                              gear_pos=GearPosition.DRIVE,
                                                              battery=BatteryState.READY))
        steps.acceleration_pedal.set_acc_pedal_pos(AccPedalPosState.PERCENT_30)
        steps.vehicle_state.assert_vehicle_state(VehicleState(brake_pedal=BrakePedalState.RELEASED,
                                                              acc_pedal=AccPedalPosState.PERCENT_30,
                                                              req_torque=ReqTorque.Nm_3000,
                                                              gear_pos=GearPosition.DRIVE,
                                                              battery=BatteryState.READY))
