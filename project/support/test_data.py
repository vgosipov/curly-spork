from project.models.pin import Pin
from . import constants

GEAR_PINS_VOLTAGE = {
    constants.GearPosition.PARK: (0.67, 3.12),
    constants.GearPosition.NEUTRAL: (1.48, 2.28),
    constants.GearPosition.REVERSE: (2.28, 1.48),
    constants.GearPosition.DRIVE: (3.12, 0.67)
}

BATTERY_PIN = {
    constants.BatteryState.READY: Pin(pin_id=constants.BATTERY_PIN_ID, voltage=450),
    constants.BatteryState.NOT_READY: Pin(pin_id=constants.BATTERY_PIN_ID, voltage=200),
    constants.BatteryState.ERROR: Pin(pin_id=constants.BATTERY_PIN_ID, voltage=0)
}

BRAKE_PEDAL_PIN = {
    constants.BrakePedalState.PRESSED: Pin(pin_id=constants.BRAKE_PEDAL_PIN_ID, voltage=1.5),
    constants.BrakePedalState.RELEASED: Pin(pin_id=constants.BRAKE_PEDAL_PIN_ID, voltage=2.5),
    constants.BrakePedalState.ERROR: Pin(pin_id=constants.BRAKE_PEDAL_PIN_ID, voltage=0.5)
}

ACC_PEDAL_PIN = {
    constants.AccPedalPosState.PERCENT_0: Pin(pin_id=constants.ACC_PEDAL_PIN_ID, voltage=1.5),
    constants.AccPedalPosState.PERCENT_30: Pin(pin_id=constants.ACC_PEDAL_PIN_ID, voltage=2.3),
    constants.AccPedalPosState.PERCENT_50: Pin(pin_id=constants.ACC_PEDAL_PIN_ID, voltage=2.7),
    constants.AccPedalPosState.PERCENT_100: Pin(pin_id=constants.ACC_PEDAL_PIN_ID, voltage=3.2),
    constants.AccPedalPosState.ERROR: Pin(pin_id=constants.ACC_PEDAL_PIN_ID, voltage=0.2),
}

GEAR_PINS = {
    constants.GearPosition.PARK:
        (Pin(pin_id=constants.GEAR_1_PIN_ID, voltage=GEAR_PINS_VOLTAGE[constants.GearPosition.PARK][0]),
         Pin(pin_id=constants.GEAR_2_PIN_ID, voltage=GEAR_PINS_VOLTAGE[constants.GearPosition.PARK][1])),

    constants.GearPosition.NEUTRAL:
        (Pin(pin_id=constants.GEAR_1_PIN_ID, voltage=GEAR_PINS_VOLTAGE[constants.GearPosition.NEUTRAL][0]),
         Pin(pin_id=constants.GEAR_2_PIN_ID, voltage=GEAR_PINS_VOLTAGE[constants.GearPosition.NEUTRAL][1])),

    constants.GearPosition.REVERSE:
        (Pin(pin_id=constants.GEAR_1_PIN_ID, voltage=GEAR_PINS_VOLTAGE[constants.GearPosition.REVERSE][0]),
         Pin(pin_id=constants.GEAR_2_PIN_ID, voltage=GEAR_PINS_VOLTAGE[constants.GearPosition.REVERSE][1])),

    constants.GearPosition.DRIVE:
        (Pin(pin_id=constants.GEAR_1_PIN_ID, voltage=GEAR_PINS_VOLTAGE[constants.GearPosition.DRIVE][0]),
         Pin(pin_id=constants.GEAR_2_PIN_ID, voltage=GEAR_PINS_VOLTAGE[constants.GearPosition.DRIVE][1]))
}

