from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pricing_billing_term import PricingBillingTerm
from ..models.pricing_type import PricingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Pricing")


@attr.s(auto_attribs=True)
class Pricing:
    """
    Attributes:
        billing_term (Union[Unset, PricingBillingTerm]):
        type (Union[Unset, PricingType]):
        unit_of_measurement (Union[Unset, str]): The unit of measurement Example: Each.
        rates (Union[Unset, Any]): A list of rates
    """

    billing_term: Union[Unset, PricingBillingTerm] = UNSET
    type: Union[Unset, PricingType] = UNSET
    unit_of_measurement: Union[Unset, str] = UNSET
    rates: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billing_term: Union[Unset, str] = UNSET
        if not isinstance(self.billing_term, Unset):
            billing_term = self.billing_term.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        unit_of_measurement = self.unit_of_measurement
        rates = self.rates

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_term is not UNSET:
            field_dict["billingTerm"] = billing_term
        if type is not UNSET:
            field_dict["type"] = type
        if unit_of_measurement is not UNSET:
            field_dict["unitOfMeasurement"] = unit_of_measurement
        if rates is not UNSET:
            field_dict["rates"] = rates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _billing_term = d.pop("billingTerm", UNSET)
        billing_term: Union[Unset, PricingBillingTerm]
        if isinstance(_billing_term, Unset):
            billing_term = UNSET
        else:
            billing_term = PricingBillingTerm(_billing_term)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PricingType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PricingType(_type)

        unit_of_measurement = d.pop("unitOfMeasurement", UNSET)

        rates = d.pop("rates", UNSET)

        pricing = cls(
            billing_term=billing_term,
            type=type,
            unit_of_measurement=unit_of_measurement,
            rates=rates,
        )

        pricing.additional_properties = d
        return pricing

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
