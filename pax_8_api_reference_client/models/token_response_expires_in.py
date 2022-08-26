from enum import IntEnum


class TokenResponseExpiresIn(IntEnum):
    VALUE_86400 = 86400

    def __str__(self) -> str:
        return str(self.value)
