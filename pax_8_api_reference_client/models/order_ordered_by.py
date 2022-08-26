from enum import Enum


class OrderOrderedBy(str, Enum):
    PAX8_PARTNER = "Pax8 Partner"
    CUSTOMER = "Customer"
    PAX8 = "Pax8"

    def __str__(self) -> str:
        return str(self.value)
