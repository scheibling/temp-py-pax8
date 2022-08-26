import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.line_item_billing_term import LineItemBillingTerm
from ..models.provisioning_detail import ProvisioningDetail
from ..types import UNSET, Unset

T = TypeVar("T", bound="LineItem")


@attr.s(auto_attribs=True)
class LineItem:
    """
    Attributes:
        product_id (str):
        line_item_number (float): Required. Number used as a reference to the line item for parent line items Example:
            1.
        id (Union[Unset, str]):
        subscription_id (Union[Unset, str]):
        commitment_term_id (Union[Unset, str]):
        provision_start_date (Union[Unset, datetime.date]):
        billing_term (Union[Unset, LineItemBillingTerm]):
        parent_subscription_id (Union[Unset, str]): Reference to the subscription this item depends on
        parent_line_item_number (Union[Unset, float]): Reference to the required parent line item in this same order
            Example: 1.
        quantity (Union[Unset, float]): Whole Number Example: 45.
        provisioning_details (Union[Unset, List[ProvisioningDetail]]):
    """

    product_id: str
    line_item_number: float
    id: Union[Unset, str] = UNSET
    subscription_id: Union[Unset, str] = UNSET
    commitment_term_id: Union[Unset, str] = UNSET
    provision_start_date: Union[Unset, datetime.date] = UNSET
    billing_term: Union[Unset, LineItemBillingTerm] = UNSET
    parent_subscription_id: Union[Unset, str] = UNSET
    parent_line_item_number: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    provisioning_details: Union[Unset, List[ProvisioningDetail]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id
        line_item_number = self.line_item_number
        id = self.id
        subscription_id = self.subscription_id
        commitment_term_id = self.commitment_term_id
        provision_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.provision_start_date, Unset):
            provision_start_date = self.provision_start_date.isoformat()

        billing_term: Union[Unset, str] = UNSET
        if not isinstance(self.billing_term, Unset):
            billing_term = self.billing_term.value

        parent_subscription_id = self.parent_subscription_id
        parent_line_item_number = self.parent_line_item_number
        quantity = self.quantity
        provisioning_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.provisioning_details, Unset):
            provisioning_details = []
            for provisioning_details_item_data in self.provisioning_details:
                provisioning_details_item = provisioning_details_item_data.to_dict()

                provisioning_details.append(provisioning_details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productId": product_id,
                "lineItemNumber": line_item_number,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if commitment_term_id is not UNSET:
            field_dict["commitmentTermId"] = commitment_term_id
        if provision_start_date is not UNSET:
            field_dict["provisionStartDate"] = provision_start_date
        if billing_term is not UNSET:
            field_dict["billingTerm"] = billing_term
        if parent_subscription_id is not UNSET:
            field_dict["parentSubscriptionId"] = parent_subscription_id
        if parent_line_item_number is not UNSET:
            field_dict["parentLineItemNumber"] = parent_line_item_number
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if provisioning_details is not UNSET:
            field_dict["provisioningDetails"] = provisioning_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_id = d.pop("productId")

        line_item_number = d.pop("lineItemNumber")

        id = d.pop("id", UNSET)

        subscription_id = d.pop("subscriptionId", UNSET)

        commitment_term_id = d.pop("commitmentTermId", UNSET)

        _provision_start_date = d.pop("provisionStartDate", UNSET)
        provision_start_date: Union[Unset, datetime.date]
        if isinstance(_provision_start_date, Unset):
            provision_start_date = UNSET
        else:
            provision_start_date = isoparse(_provision_start_date).date()

        _billing_term = d.pop("billingTerm", UNSET)
        billing_term: Union[Unset, LineItemBillingTerm]
        if isinstance(_billing_term, Unset):
            billing_term = UNSET
        else:
            billing_term = LineItemBillingTerm(_billing_term)

        parent_subscription_id = d.pop("parentSubscriptionId", UNSET)

        parent_line_item_number = d.pop("parentLineItemNumber", UNSET)

        quantity = d.pop("quantity", UNSET)

        provisioning_details = []
        _provisioning_details = d.pop("provisioningDetails", UNSET)
        for provisioning_details_item_data in _provisioning_details or []:
            provisioning_details_item = ProvisioningDetail.from_dict(provisioning_details_item_data)

            provisioning_details.append(provisioning_details_item)

        line_item = cls(
            product_id=product_id,
            line_item_number=line_item_number,
            id=id,
            subscription_id=subscription_id,
            commitment_term_id=commitment_term_id,
            provision_start_date=provision_start_date,
            billing_term=billing_term,
            parent_subscription_id=parent_subscription_id,
            parent_line_item_number=parent_line_item_number,
            quantity=quantity,
            provisioning_details=provisioning_details,
        )

        line_item.additional_properties = d
        return line_item

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
