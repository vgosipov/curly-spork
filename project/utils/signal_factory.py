from project.models.signal import Signal
from project.support import constants


class SignalFactory:
    @staticmethod
    def gear_pos(*, value):
        return Signal(name=constants.GEAR_POS_SIG_NAME, sig_id=constants.GEAR_POS_SIG_ID, value=value)

    @staticmethod
    def req_torque(*, value):
        return Signal(name=constants.REQ_TORQUE_SIG_NAME, sig_id=constants.REQ_TORQUE_SIG_ID, value=value)

    @staticmethod
    def brake_pedal(*, value):
        return Signal(name=constants.BRAKE_PEDAL_SIG_NAME, sig_id=constants.BRAKE_PEDAL_SIG_ID, value=value)

    @staticmethod
    def acc_pedal(*, value):
        return Signal(name=constants.ACC_PEDAL_SIG_NAME, sig_id=constants.ACC_PEDAL_POS_SIG_ID, value=value)

    @staticmethod
    def battery_state(*, value):
        return Signal(name=constants.BATTERY_SIG_NAME, sig_id=constants.BATTERY_SIG_ID, value=value)
