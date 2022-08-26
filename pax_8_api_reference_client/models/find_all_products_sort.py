from enum import Enum


class FindAllProductsSort(str, Enum):
    NAME = "name"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
