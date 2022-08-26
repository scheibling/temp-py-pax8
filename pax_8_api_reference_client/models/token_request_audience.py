from enum import Enum


class TokenRequestAudience(str, Enum):
    APIP8P_CLIENT = "api://p8p.client"

    def __str__(self) -> str:
        return str(self.value)
