from enum import Enum


class ProvisioningDetailValueType(str, Enum):
    INPUT = "Input"
    SINGLE_VALUE = "Single-Value"
    MULTI_VALUE = "Multi-Value"

    def __str__(self) -> str:
        return str(self.value)
