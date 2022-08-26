from enum import Enum


class ContactTypeType(str, Enum):
    ADMIN = "Admin"
    BILLING = "Billing"
    TECHNICAL = "Technical"

    def __str__(self) -> str:
        return str(self.value)
