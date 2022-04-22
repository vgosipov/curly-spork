from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass(init=True, eq=True)
class Pin:
    pin_id: int
    voltage: float
    name: str = None
