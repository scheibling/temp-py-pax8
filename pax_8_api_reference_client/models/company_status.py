from enum import Enum


class CompanyStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    DELETED = "Deleted"

    def __str__(self) -> str:
        return str(self.value)
