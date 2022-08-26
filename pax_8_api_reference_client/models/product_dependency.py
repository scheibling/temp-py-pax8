from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.product import Product
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductDependency")


@attr.s(auto_attribs=True)
class ProductDependency:
    """
    Attributes:
        name (Union[Unset, str]): The name of the product constraint
        products (Union[Unset, List[Product]]): A list of products that satisfy the constraint
    """

    name: Union[Unset, str] = UNSET
    products: Union[Unset, List[Product]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()

                products.append(products_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = Product.from_dict(products_item_data)

            products.append(products_item)

        product_dependency = cls(
            name=name,
            products=products,
        )

        product_dependency.additional_properties = d
        return product_dependency

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
