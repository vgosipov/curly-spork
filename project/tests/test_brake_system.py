import allure
import pytest

from project.models.vehicle_state import VehicleState
from project.support.constants import BatteryState, BrakePedalState


class TestBrakeSystem:
    @allure.title('25. Тормозная система реагирует корректно на изменение напряжения при низком напряжении батареи')
    @pytest.mark.parametrize('voltage,expected_brake_pedal_pos', [(0, BrakePedalState.ERROR),
                                                                  (0.99, BrakePedalState.ERROR),
                                                                  (1, BrakePedalState.PRESSED),
                                                                  (1.01, BrakePedalState.PRESSED),
                                                                  (1.5, BrakePedalState.PRESSED),
                                                                  (1.99, BrakePedalState.PRESSED),
                                                                  (2, BrakePedalState.RELEASED),
                                                                  (2.01, BrakePedalState.RELEASED),
                                                                  (2.5, BrakePedalState.RELEASED),
                                                                  (2.99, BrakePedalState.RELEASED),
                                                                  (3, BrakePedalState.ERROR),
                                                                  (3.01, BrakePedalState.ERROR),
                                                                  (4, BrakePedalState.ERROR)])
    def test_scenario_24_break_pedal_reacts_on_voltage_change(self, steps, voltage, expected_brake_pedal_pos):
        steps.vehicle_state.set_vehicle_state(VehicleState(battery=BatteryState.NOT_READY))
        steps.brake_pedal.set_brake_pedal_pin(voltage)
        steps.brake_pedal.assert_brake_pedal_signal(expected_brake_pedal_pos)
