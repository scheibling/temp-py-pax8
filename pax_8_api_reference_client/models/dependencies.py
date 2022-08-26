from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.commitment import Commitment
from ..models.product_dependency import ProductDependency
from ..types import UNSET, Unset

T = TypeVar("T", bound="Dependencies")


@attr.s(auto_attribs=True)
class Dependencies:
    """
    Attributes:
        commitment_dependencies (Union[Unset, List[Commitment]]):
        product_dependencies (Union[Unset, List[ProductDependency]]):
    """

    commitment_dependencies: Union[Unset, List[Commitment]] = UNSET
    product_dependencies: Union[Unset, List[ProductDependency]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commitment_dependencies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.commitment_dependencies, Unset):
            commitment_dependencies = []
            for commitment_dependencies_item_data in self.commitment_dependencies:
                commitment_dependencies_item = commitment_dependencies_item_data.to_dict()

                commitment_dependencies.append(commitment_dependencies_item)

        product_dependencies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.product_dependencies, Unset):
            product_dependencies = []
            for product_dependencies_item_data in self.product_dependencies:
                product_dependencies_item = product_dependencies_item_data.to_dict()

                product_dependencies.append(product_dependencies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commitment_dependencies is not UNSET:
            field_dict["commitmentDependencies"] = commitment_dependencies
        if product_dependencies is not UNSET:
            field_dict["productDependencies"] = product_dependencies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        commitment_dependencies = []
        _commitment_dependencies = d.pop("commitmentDependencies", UNSET)
        for commitment_dependencies_item_data in _commitment_dependencies or []:
            commitment_dependencies_item = Commitment.from_dict(commitment_dependencies_item_data)

            commitment_dependencies.append(commitment_dependencies_item)

        product_dependencies = []
        _product_dependencies = d.pop("productDependencies", UNSET)
        for product_dependencies_item_data in _product_dependencies or []:
            product_dependencies_item = ProductDependency.from_dict(product_dependencies_item_data)

            product_dependencies.append(product_dependencies_item)

        dependencies = cls(
            commitment_dependencies=commitment_dependencies,
            product_dependencies=product_dependencies,
        )

        dependencies.additional_properties = d
        return dependencies

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
