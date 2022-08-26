from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionCommitment")


@attr.s(auto_attribs=True)
class SubscriptionCommitment:
    """
    Attributes:
        id (Union[Unset, str]): Unique identifier for the commitment record
        term (Union[Unset, str]): Duration of the commitment Example: 3-Year.
        end_date (Union[Unset, str]):  Example: 2023-05-12.
    """

    id: Union[Unset, str] = UNSET
    term: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        term = self.term
        end_date = self.end_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if term is not UNSET:
            field_dict["term"] = term
        if end_date is not UNSET:
            field_dict["endDate"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        term = d.pop("term", UNSET)

        end_date = d.pop("endDate", UNSET)

        subscription_commitment = cls(
            id=id,
            term=term,
            end_date=end_date,
        )

        subscription_commitment.additional_properties = d
        return subscription_commitment

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
