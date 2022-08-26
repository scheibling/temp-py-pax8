from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rate_charge_type import RateChargeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Rate")


@attr.s(auto_attribs=True)
class Rate:
    """
    Attributes:
        partner_buy_rate (Union[Unset, float]): The partner cost Example: 145.8.
        suggested_retail_price (Union[Unset, float]): The suggested customer cost Example: 151.8.
        start_quantity_range (Union[Unset, float]): The start of the quantity range. If not set 0 is the default
            Example: 5.
        end_quantity_range (Union[Unset, float]): The end of the quantity range. If ```null``` there is no end of range
            Example: 200.
        charge_type (Union[Unset, RateChargeType]): Rate Charge Type:
              * `Per Unit` - The rate is multiplied directly by the quantity based on the start and end quantity range
              * `Flat Rate` - The rate is flat for the quantity based on the start and end quantity range
    """

    partner_buy_rate: Union[Unset, float] = UNSET
    suggested_retail_price: Union[Unset, float] = UNSET
    start_quantity_range: Union[Unset, float] = UNSET
    end_quantity_range: Union[Unset, float] = UNSET
    charge_type: Union[Unset, RateChargeType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        partner_buy_rate = self.partner_buy_rate
        suggested_retail_price = self.suggested_retail_price
        start_quantity_range = self.start_quantity_range
        end_quantity_range = self.end_quantity_range
        charge_type: Union[Unset, str] = UNSET
        if not isinstance(self.charge_type, Unset):
            charge_type = self.charge_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if partner_buy_rate is not UNSET:
            field_dict["partnerBuyRate"] = partner_buy_rate
        if suggested_retail_price is not UNSET:
            field_dict["suggestedRetailPrice"] = suggested_retail_price
        if start_quantity_range is not UNSET:
            field_dict["startQuantityRange"] = start_quantity_range
        if end_quantity_range is not UNSET:
            field_dict["endQuantityRange"] = end_quantity_range
        if charge_type is not UNSET:
            field_dict["chargeType"] = charge_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        partner_buy_rate = d.pop("partnerBuyRate", UNSET)

        suggested_retail_price = d.pop("suggestedRetailPrice", UNSET)

        start_quantity_range = d.pop("startQuantityRange", UNSET)

        end_quantity_range = d.pop("endQuantityRange", UNSET)

        _charge_type = d.pop("chargeType", UNSET)
        charge_type: Union[Unset, RateChargeType]
        if isinstance(_charge_type, Unset):
            charge_type = UNSET
        else:
            charge_type = RateChargeType(_charge_type)

        rate = cls(
            partner_buy_rate=partner_buy_rate,
            suggested_retail_price=suggested_retail_price,
            start_quantity_range=start_quantity_range,
            end_quantity_range=end_quantity_range,
            charge_type=charge_type,
        )

        rate.additional_properties = d
        return rate

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
