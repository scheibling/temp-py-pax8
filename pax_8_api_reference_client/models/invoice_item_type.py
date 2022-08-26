from enum import Enum


class InvoiceItemType(str, Enum):
    REBATE = "rebate"
    PRORATE = "prorate"
    SUBSCRIPTION = "subscription"
    PAYMENT_CREDIT = "payment-credit"
    ONE_TIME = "one-time"
    SERVICE_CHARGE = "service-charge"
    SERVICE_CREDIT = "service-credit"
    INVOICE_CREDIT = "invoice-credit"

    def __str__(self) -> str:
        return str(self.value)
