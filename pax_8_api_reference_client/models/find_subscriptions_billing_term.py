from enum import Enum


class FindSubscriptionsBillingTerm(str, Enum):
    MONTHLY = "Monthly"
    ANNUAL = "Annual"
    VALUE_2 = "2-Year"
    VALUE_3 = "3-Year"
    ONE_TIME = "One-Time"
    TRIAL = "Trial"
    ACTIVATION = "Activation"

    def __str__(self) -> str:
        return str(self.value)
