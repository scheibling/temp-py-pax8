from enum import Enum


class PricingType(str, Enum):
    FLAT = "Flat"
    VOLUME = "Volume"
    TIERED = "Tiered"
    MARK_UP = "Mark-Up"

    def __str__(self) -> str:
        return str(self.value)
