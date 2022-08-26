from enum import Enum


class FindCompaniesStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    DELETED = "Deleted"

    def __str__(self) -> str:
        return str(self.value)
