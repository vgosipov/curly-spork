from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass(init=True, eq=True)
class Signal:
    sig_id: int
    value: str
    name: str = None
