from project.models.pin import Pin
from project.support import constants


class PinFactory:
    @staticmethod
    def gear_1(*, voltage):
        return Pin(name=constants.GEAR_1_PIN_NAME, pin_id=constants.GEAR_1_PIN_ID, voltage=voltage)

    @staticmethod
    def gear_2(*, voltage):
        return Pin(name=constants.GEAR_2_PIN_NAME, pin_id=constants.GEAR_2_PIN_ID, voltage=voltage)

    @staticmethod
    def brake_pedal(*, voltage):
        return Pin(name=constants.BRAKE_PEDAL_PIN_NAME, pin_id=constants.BRAKE_PEDAL_PIN_ID, voltage=voltage)

    @staticmethod
    def acc_pedal(*, voltage):
        return Pin(name=constants.ACC_PEDAL_PIN_NAME, pin_id=constants.ACC_PEDAL_PIN_ID, voltage=voltage)
