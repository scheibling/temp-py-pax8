import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.line_item import LineItem
from ..models.order_ordered_by import OrderOrderedBy
from ..types import UNSET, Unset

T = TypeVar("T", bound="Order")


@attr.s(auto_attribs=True)
class Order:
    """
    Attributes:
        company_id (str): unique id of the purchasing company ie. end-user
        line_items (List[LineItem]):
        id (Union[Unset, str]): unique id of the order
        created_date (Union[Unset, datetime.date]): the date the order was created
        ordered_by (Union[Unset, OrderOrderedBy]): the type of user who created the order
        ordered_by_user_id (Union[Unset, str]): unique id of the user who created this order
        ordered_by_user_email (Union[Unset, str]): the email address of the user who created this order Example:
            john@doe.com.
    """

    company_id: str
    line_items: List[LineItem]
    id: Union[Unset, str] = UNSET
    created_date: Union[Unset, datetime.date] = UNSET
    ordered_by: Union[Unset, OrderOrderedBy] = UNSET
    ordered_by_user_id: Union[Unset, str] = UNSET
    ordered_by_user_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()

            line_items.append(line_items_item)

        id = self.id
        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        ordered_by: Union[Unset, str] = UNSET
        if not isinstance(self.ordered_by, Unset):
            ordered_by = self.ordered_by.value

        ordered_by_user_id = self.ordered_by_user_id
        ordered_by_user_email = self.ordered_by_user_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
                "lineItems": line_items,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if ordered_by is not UNSET:
            field_dict["orderedBy"] = ordered_by
        if ordered_by_user_id is not UNSET:
            field_dict["orderedByUserId"] = ordered_by_user_id
        if ordered_by_user_email is not UNSET:
            field_dict["orderedByUserEmail"] = ordered_by_user_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        company_id = d.pop("companyId")

        line_items = []
        _line_items = d.pop("lineItems")
        for line_items_item_data in _line_items:
            line_items_item = LineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        id = d.pop("id", UNSET)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.date]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date).date()

        _ordered_by = d.pop("orderedBy", UNSET)
        ordered_by: Union[Unset, OrderOrderedBy]
        if isinstance(_ordered_by, Unset):
            ordered_by = UNSET
        else:
            ordered_by = OrderOrderedBy(_ordered_by)

        ordered_by_user_id = d.pop("orderedByUserId", UNSET)

        ordered_by_user_email = d.pop("orderedByUserEmail", UNSET)

        order = cls(
            company_id=company_id,
            line_items=line_items,
            id=id,
            created_date=created_date,
            ordered_by=ordered_by,
            ordered_by_user_id=ordered_by_user_id,
            ordered_by_user_email=ordered_by_user_email,
        )

        order.additional_properties = d
        return order

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
