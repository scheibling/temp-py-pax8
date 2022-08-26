from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.contact_type_type import ContactTypeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactType")


@attr.s(auto_attribs=True)
class ContactType:
    """
    Attributes:
        type (Union[Unset, ContactTypeType]): A company must have a primary contact for each contact type. A single
            contact can be marked as a primary contact for all types
            Contact Type:
              * `Admin` - Administrative contact
              * `Billing` - Billing contact
              * `Technical` - Technical contact
        primary (Union[Unset, bool]): Is this contact the primary contact for this Contact Type
    """

    type: Union[Unset, ContactTypeType] = UNSET
    primary: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        primary = self.primary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, ContactTypeType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ContactTypeType(_type)

        primary = d.pop("primary", UNSET)

        contact_type = cls(
            type=type,
            primary=primary,
        )

        contact_type.additional_properties = d
        return contact_type

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
