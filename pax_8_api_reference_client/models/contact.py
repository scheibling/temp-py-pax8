from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.contact_type import ContactType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Contact")


@attr.s(auto_attribs=True)
class Contact:
    """
    Attributes:
        first_name (str): The first name Example: John.
        last_name (str): The last name Example: Doe.
        email (str): The email Example: john@doe.com.
        phone (str): The phone number Example: 555-555-5555.
        id (Union[Unset, str]): The id Example: 18d6329e-93f9-46a5-9df7-37e4c29d2840.
        created_date (Union[Unset, str]): The created date Example: 2020-05-12.
        types (Union[Unset, List[ContactType]]):
    """

    first_name: str
    last_name: str
    email: str
    phone: str
    id: Union[Unset, str] = UNSET
    created_date: Union[Unset, str] = UNSET
    types: Union[Unset, List[ContactType]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        phone = self.phone
        id = self.id
        created_date = self.created_date
        types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.types, Unset):
            types = []
            for types_item_data in self.types:
                types_item = types_item_data.to_dict()

                types.append(types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "phone": phone,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if types is not UNSET:
            field_dict["types"] = types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        email = d.pop("email")

        phone = d.pop("phone")

        id = d.pop("id", UNSET)

        created_date = d.pop("createdDate", UNSET)

        types = []
        _types = d.pop("types", UNSET)
        for types_item_data in _types or []:
            types_item = ContactType.from_dict(types_item_data)

            types.append(types_item)

        contact = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            id=id,
            created_date=created_date,
            types=types,
        )

        contact.additional_properties = d
        return contact

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
