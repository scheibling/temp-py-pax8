from enum import Enum


class RateChargeType(str, Enum):
    PER_UNIT = "Per Unit"
    FLAT_RATE = "Flat Rate"

    def __str__(self) -> str:
        return str(self.value)
