from enum import Enum


class FindCompaniesSort(str, Enum):
    NAME = "name"
    CITY = "city"
    COUNTRY = "country"
    STATEORPROVINCE = "stateOrProvince"
    POSTALCODE = "postalCode"

    def __str__(self) -> str:
        return str(self.value)
