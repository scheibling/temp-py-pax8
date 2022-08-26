from enum import Enum


class FindSubscriptionUsageSummariesSort(str, Enum):
    RESOURCEGROUP = "resourceGroup"
    CURRENTCHARGES = "currentCharges"
    PARTNERTOTAL = "partnerTotal"

    def __str__(self) -> str:
        return str(self.value)
