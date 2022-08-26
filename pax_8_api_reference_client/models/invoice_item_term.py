from enum import Enum


class InvoiceItemTerm(str, Enum):
    VALUE_0 = "3 Year"
    ANNUAL = "Annual"
    VALUE_2 = "2 Year"
    ACTIVATION = "Activation"
    ONE_TIME = "One-time"
    ARREARS = "Arrears"
    TRIAL = "Trial"
    REBATE = "Rebate"
    MONTHLY = "Monthly"

    def __str__(self) -> str:
        return str(self.value)
