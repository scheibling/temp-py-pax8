from enum import Enum


class FindSubscriptionsSort(str, Enum):
    QUANTITY = "quantity"
    STARTDATE = "startDate"
    ENDDATE = "endDate"
    CREATEDDATE = "createdDate"
    BILLINGSTART = "billingStart"
    PRICE = "price"

    def __str__(self) -> str:
        return str(self.value)
