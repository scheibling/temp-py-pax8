from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@attr.s(auto_attribs=True)
class Address:
    """
    Attributes:
        street (Union[Unset, str]): The primary street information Example: 5500 S Quebec St.
        street2 (Union[Unset, str]): The secondary street information Example: Ste. 350.
        city (Union[Unset, str]): The city Example: Greenwood Village.
        state_or_province (Union[Unset, str]): The state or province Example: CO.
        postal_code (Union[Unset, str]): The postal code Example: 80111.
        country (Union[Unset, str]): The country Example: US.
    """

    street: Union[Unset, str] = UNSET
    street2: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state_or_province: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        street = self.street
        street2 = self.street2
        city = self.city
        state_or_province = self.state_or_province
        postal_code = self.postal_code
        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if street is not UNSET:
            field_dict["street"] = street
        if street2 is not UNSET:
            field_dict["street2"] = street2
        if city is not UNSET:
            field_dict["city"] = city
        if state_or_province is not UNSET:
            field_dict["stateOrProvince"] = state_or_province
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        street = d.pop("street", UNSET)

        street2 = d.pop("street2", UNSET)

        city = d.pop("city", UNSET)

        state_or_province = d.pop("stateOrProvince", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        country = d.pop("country", UNSET)

        address = cls(
            street=street,
            street2=street2,
            city=city,
            state_or_province=state_or_province,
            postal_code=postal_code,
            country=country,
        )

        address.additional_properties = d
        return address

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
