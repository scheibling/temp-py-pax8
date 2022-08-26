from enum import Enum


class FindSubscriptionsStatus(str, Enum):
    ACTIVE = "Active"
    CANCELLED = "Cancelled"
    PENDINGMANUAL = "PendingManual"
    PENDINGAUTOMATED = "PendingAutomated"
    PENDINGCANCEL = "PendingCancel"
    WAITINGFORDETAILS = "WaitingForDetails"
    TRIAL = "Trial"
    CONVERTED = "Converted"
    PENDINGACTIVATION = "PendingActivation"
    ACTIVATED = "Activated"

    def __str__(self) -> str:
        return str(self.value)
