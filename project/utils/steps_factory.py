from project.api import VehicleApi
from project.steps import AccelerationPedalSteps, VehicleApiSteps, GearPosSteps, BrakePedalSteps, BatterySteps, \
    VehicleStateSteps
from project.utils.pin_factory import PinFactory
from project.utils.signal_factory import SignalFactory


class StepsFactory:
    def __init__(self, api: VehicleApi, pin_factory: PinFactory, signal_factory: SignalFactory):
        self.api = api
        self.pin_factory = pin_factory
        self.signal_factory = signal_factory

    @property
    def acceleration_pedal(self) -> AccelerationPedalSteps:
        return AccelerationPedalSteps(self.api, self.pin_factory, self.signal_factory)

    @property
    def battery(self) -> BatterySteps:
        return BatterySteps(self.api, self.pin_factory, self.signal_factory)

    @property
    def brake_pedal(self) -> BrakePedalSteps:
        return BrakePedalSteps(self.api, self.pin_factory, self.signal_factory)

    @property
    def gear_pos(self) -> GearPosSteps:
        return GearPosSteps(self.api, self.pin_factory, self.signal_factory)

    @property
    def vehicle_api(self) -> VehicleApiSteps:
        return VehicleApiSteps(self.api)

    @property
    def vehicle_state(self) -> VehicleStateSteps:
        return VehicleStateSteps(self.api, self.signal_factory)
