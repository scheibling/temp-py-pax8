from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Page")


@attr.s(auto_attribs=True)
class Page:
    """
    Attributes:
        size (Union[Unset, float]): The size of the page Default: 10.0. Example: 50.
        total_elements (Union[Unset, Any]): The total number of elements able to be paged over Example: 237.
        total_pages (Union[Unset, Any]): The total number of pages based on the ```size``` and ```totalElements```
            Example: 5.
        number (Union[Unset, Any]): The current page Example: 1.
    """

    size: Union[Unset, float] = 10.0
    total_elements: Union[Unset, Any] = UNSET
    total_pages: Union[Unset, Any] = UNSET
    number: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        size = self.size
        total_elements = self.total_elements
        total_pages = self.total_pages
        number = self.number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if total_elements is not UNSET:
            field_dict["totalElements"] = total_elements
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        size = d.pop("size", UNSET)

        total_elements = d.pop("totalElements", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        number = d.pop("number", UNSET)

        page = cls(
            size=size,
            total_elements=total_elements,
            total_pages=total_pages,
            number=number,
        )

        page.additional_properties = d
        return page

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
