from dataclasses import dataclass


@dataclass
class VehicleState:
    battery: str = None
    gear_pos: str = None
    brake_pedal: str = None
    acc_pedal: str = None
    req_torque: str = None
