import allure
import pytest

from project.models.vehicle_state import VehicleState
from project.support.constants import GearPosition, BatteryState, BrakePedalState, AccPedalPosState


class TestGearPosSystem:
    @allure.title('18. Переключение передачи в "{gear}"')
    @pytest.mark.parametrize('gear', (GearPosition.PARK, GearPosition.DRIVE,
                                      GearPosition.NEUTRAL, GearPosition.REVERSE))
    def test_scenario_18_select_gear(self, steps, gear):
        steps.vehicle_state.set_vehicle_state(VehicleState(battery=BatteryState.READY,
                                                           brake_pedal=BrakePedalState.PRESSED,
                                                           acc_pedal=AccPedalPosState.PERCENT_0))
        steps.gear_pos.set_gear(gear)
        steps.gear_pos.assert_gear_pos_signal(gear)
