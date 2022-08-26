from enum import Enum


class InvoiceItemRateType(str, Enum):
    MARKUP_PERCENTAGE_BASED_MARKUP_OVER_TO_BE_DETERMINED_BASE_COST = (
        "markup (Percentage based markup over to be determined base cost)"
    )
    SINGLE_SINGLE_PRICE_FOR_ANY_QUANTITY_SAME_AS_FLAT = "single (Single price for any quantity, same as flat)"
    FLAT_SINGLE_PRICE_FOR_ANY_QUANTITY_SAME_AS_SINGLE = "flat (Single price for any quantity, same as single)"
    VOLUME_PRICE_SCALES_LINEARLY_WITH_QUANTITY = "volume (Price scales linearly with quantity)"
    TIERED_PRICE_DEPENDANT_ON_QUANTITY = "tiered (Price dependant on quantity)"

    def __str__(self) -> str:
        return str(self.value)
