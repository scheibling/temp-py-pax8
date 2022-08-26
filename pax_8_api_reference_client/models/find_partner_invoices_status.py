from enum import Enum


class FindPartnerInvoicesStatus(str, Enum):
    UNPAID = "Unpaid"
    PAID = "Paid"
    VOID = "Void"
    CARRIED = "Carried"
    NOTHING_DUE = "Nothing Due"

    def __str__(self) -> str:
        return str(self.value)
