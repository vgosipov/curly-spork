from typing import Union, Sequence

from framework.api import ApiBase
from project.models.pin import Pin
from project.models.signal import Signal


class VehicleApi(ApiBase):
    BASE_URL = 'http://localhost'
    PINS_URL = '/api/pins'
    PIN_URL = '/api/pins/{0}'
    UPDATE_PIN_URL = '/api/pins/{0}/update_pin'
    UPDATE_PINS_URL = '/api/pins/update_pins'
    SIGNALS_URL = '/api/signals'
    SIGNAL_URL = '/api/signals/{0}'

    def __init__(self, base_url: str):
        self.BASE_URL = base_url.rstrip('/')
        super().__init__()

    def update_pin(self, pin_id: Union[int, str], voltage: float) -> None:
        url = self.BASE_URL + self.UPDATE_PIN_URL.format(pin_id)
        payload = {
            'Voltage': voltage
        }
        self._post(url, data=payload)

    def update_pins(self, *pins: Pin) -> None:
        url = self.BASE_URL + self.UPDATE_PINS_URL
        payload = {
            'Pins': Pin.schema().dump(pins, many=True)
        }
        self._post(url, json=payload)

    def get_signal(self, sig_id: Union[int, str]) -> Signal:
        url = self.BASE_URL + self.SIGNAL_URL.format(sig_id)
        response = self._get(url)
        return Signal.from_dict(response.json())

    def get_signals(self) -> Sequence[Signal]:
        url = self.BASE_URL + self.SIGNALS_URL
        response = self._get(url)
        return Signal.schema().loads(response.text, many=True)

    def get_pin(self, pin_id: Union[int, str]) -> Pin:
        url = self.BASE_URL + self.PIN_URL.format(pin_id)
        response = self._get(url)
        return Pin.schema().loads(response.text, many=True)

    def get_pins(self) -> Sequence[Pin]:
        url = self.BASE_URL + self.PINS_URL
        response = self._get(url)
        return Pin.schema().loads(response.text, many=True)
