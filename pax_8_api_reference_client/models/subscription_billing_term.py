from enum import Enum


class SubscriptionBillingTerm(str, Enum):
    MONTHLY = "Monthly"
    ANNUAL = "Annual"
    VALUE_2 = "2-Year"
    VALUE_3 = "3-Year"
    VALUE_4 = "1-Time"
    TRIAL = "Trial"

    def __str__(self) -> str:
        return str(self.value)
