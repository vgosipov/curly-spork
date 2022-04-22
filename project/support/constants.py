GEAR_1_PIN_ID = 1
GEAR_2_PIN_ID = 2
ACC_PEDAL_PIN_ID = 3
BRAKE_PEDAL_PIN_ID = 4
BATTERY_PIN_ID = 5
GEAR_1_PIN_NAME = 'Gear_1'
GEAR_2_PIN_NAME = 'Gear_2'
BRAKE_PEDAL_PIN_NAME = 'BrakePedal'
ACC_PEDAL_PIN_NAME = 'AccPedal'
BATTERY_PIN_NAME = 'BatteryVoltage'

GEAR_POS_SIG_ID = 1
ACC_PEDAL_POS_SIG_ID = 2
BRAKE_PEDAL_SIG_ID = 3
REQ_TORQUE_SIG_ID = 4
BATTERY_SIG_ID = 5
GEAR_POS_SIG_NAME = 'GearPosition'
REQ_TORQUE_SIG_NAME = 'ReqTorque'
BRAKE_PEDAL_SIG_NAME = 'BrakePedalState'
ACC_PEDAL_SIG_NAME = 'AccPedalPos'
BATTERY_SIG_NAME = 'BatteryState'

GEAR_1_PIN_ZERO_VOLTAGE = 0
GEAR_2_PIN_ZERO_VOLTAGE = 0
BRAKE_PEDAL_PIN_ZERO_VOLTAGE = 0
ACC_PEDAL_PIN_ZERO_VOLTAGE = 0


class GearPosition:
    PARK = 'Park'
    REVERSE = 'Reverse'
    NEUTRAL = 'Neutral'
    DRIVE = 'Drive'


class BatteryState:
    READY = 'Ready'
    NOT_READY = 'NotReady'
    ERROR = 'Error'


class BrakePedalState:
    PRESSED = 'Pressed'
    RELEASED = 'Released'
    ERROR = 'Error'


class AccPedalPosState:
    PERCENT_0 = '0 %'
    PERCENT_30 = '30 %'
    PERCENT_50 = '50 %'
    PERCENT_100 = '100 %'
    ERROR = 'Error'


class ReqTorque:
    Nm_0 = '0 Nm'
    Nm_3000 = '3000 Nm'
    Nm_5000 = '5000 Nm'
    Nm_10000 = '10000 Nm'
