from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Product")


@attr.s(auto_attribs=True)
class Product:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]): The name of a product Example: Acme Corps Productivity Suite.
        vendor_name (Union[Unset, str]): The name of the vendor Example: Acme Corps.
        short_description (Union[Unset, str]): A short description of the product Example: Short description about the
            product to sell.
        sku (Union[Unset, str]): The product sku Example: 4225-776-3234.
        vendor_sku (Union[Unset, str]): The product vendor sku Example: 12345-AA-XYZ.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    vendor_name: Union[Unset, str] = UNSET
    short_description: Union[Unset, str] = UNSET
    sku: Union[Unset, str] = UNSET
    vendor_sku: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        vendor_name = self.vendor_name
        short_description = self.short_description
        sku = self.sku
        vendor_sku = self.vendor_sku

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if vendor_name is not UNSET:
            field_dict["vendorName"] = vendor_name
        if short_description is not UNSET:
            field_dict["shortDescription"] = short_description
        if sku is not UNSET:
            field_dict["sku"] = sku
        if vendor_sku is not UNSET:
            field_dict["vendorSku"] = vendor_sku

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        vendor_name = d.pop("vendorName", UNSET)

        short_description = d.pop("shortDescription", UNSET)

        sku = d.pop("sku", UNSET)

        vendor_sku = d.pop("vendorSku", UNSET)

        product = cls(
            id=id,
            name=name,
            vendor_name=vendor_name,
            short_description=short_description,
            sku=sku,
            vendor_sku=vendor_sku,
        )

        product.additional_properties = d
        return product

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
