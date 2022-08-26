from enum import Enum


class FindPartnerInvoicesSort(str, Enum):
    INVOICEDATE = "invoiceDate"
    DUEDATE = "dueDate"
    STATUS = "status"
    PARTNERNAME = "partnerName"
    TOTAL = "total"
    BALANCE = "balance"
    CARRIEDBALANCE = "carriedBalance"

    def __str__(self) -> str:
        return str(self.value)
