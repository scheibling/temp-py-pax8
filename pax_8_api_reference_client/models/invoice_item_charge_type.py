from enum import Enum


class InvoiceItemChargeType(str, Enum):
    FLAT = "flat"
    PER = "per"

    def __str__(self) -> str:
        return str(self.value)
