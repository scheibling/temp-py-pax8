import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.provisioning_detail import ProvisioningDetail
from ..models.subscription_billing_term import SubscriptionBillingTerm
from ..models.subscription_commitment import SubscriptionCommitment
from ..models.subscription_status import SubscriptionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Subscription")


@attr.s(auto_attribs=True)
class Subscription:
    """
    Attributes:
        quantity (float):
        start_date (datetime.date):
        billing_term (SubscriptionBillingTerm):
        id (Union[Unset, str]):
        company_id (Union[Unset, str]):
        product_id (Union[Unset, str]):
        end_date (Union[Unset, datetime.date]):
        created_date (Union[Unset, datetime.datetime]):
        updated_date (Union[Unset, datetime.datetime]):
        billing_start (Union[Unset, datetime.date]):
        status (Union[Unset, SubscriptionStatus]): Subscription Status :
             * `Active` - Provisioning request complete
             * `Cancelled` - Deprovisioning request complete
             * `PendingManual` - Manual provisioning pending
             * `PendingAutomated` - Automated provisioning pending
             * `PendingCancel` - Deprovisioning pending
             * `WaitingForDetails` - Provisioning entered without details
             * `Trial` - Trial
             * `Converted` - Converted from trial
             * `PendingActivation` - Pending activation
             * `Activated` - Activated
        price (Union[Unset, float]):  Example: 15.39.
        provisioning_details (Union[Unset, List[ProvisioningDetail]]):
        commitment_term (Union[Unset, SubscriptionCommitment]):
    """

    quantity: float
    start_date: datetime.date
    billing_term: SubscriptionBillingTerm
    id: Union[Unset, str] = UNSET
    company_id: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    updated_date: Union[Unset, datetime.datetime] = UNSET
    billing_start: Union[Unset, datetime.date] = UNSET
    status: Union[Unset, SubscriptionStatus] = UNSET
    price: Union[Unset, float] = UNSET
    provisioning_details: Union[Unset, List[ProvisioningDetail]] = UNSET
    commitment_term: Union[Unset, SubscriptionCommitment] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity
        start_date = self.start_date.isoformat()
        billing_term = self.billing_term.value

        id = self.id
        company_id = self.company_id
        product_id = self.product_id
        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.updated_date, Unset):
            updated_date = self.updated_date.isoformat()

        billing_start: Union[Unset, str] = UNSET
        if not isinstance(self.billing_start, Unset):
            billing_start = self.billing_start.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        price = self.price
        provisioning_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.provisioning_details, Unset):
            provisioning_details = []
            for provisioning_details_item_data in self.provisioning_details:
                provisioning_details_item = provisioning_details_item_data.to_dict()

                provisioning_details.append(provisioning_details_item)

        commitment_term: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.commitment_term, Unset):
            commitment_term = self.commitment_term.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
                "startDate": start_date,
                "billingTerm": billing_term,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if updated_date is not UNSET:
            field_dict["updatedDate"] = updated_date
        if billing_start is not UNSET:
            field_dict["billingStart"] = billing_start
        if status is not UNSET:
            field_dict["status"] = status
        if price is not UNSET:
            field_dict["price"] = price
        if provisioning_details is not UNSET:
            field_dict["provisioningDetails"] = provisioning_details
        if commitment_term is not UNSET:
            field_dict["commitmentTerm"] = commitment_term

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        quantity = d.pop("quantity")

        start_date = isoparse(d.pop("startDate")).date()

        billing_term = SubscriptionBillingTerm(d.pop("billingTerm"))

        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        product_id = d.pop("productId", UNSET)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        _updated_date = d.pop("updatedDate", UNSET)
        updated_date: Union[Unset, datetime.datetime]
        if isinstance(_updated_date, Unset):
            updated_date = UNSET
        else:
            updated_date = isoparse(_updated_date)

        _billing_start = d.pop("billingStart", UNSET)
        billing_start: Union[Unset, datetime.date]
        if isinstance(_billing_start, Unset):
            billing_start = UNSET
        else:
            billing_start = isoparse(_billing_start).date()

        _status = d.pop("status", UNSET)
        status: Union[Unset, SubscriptionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SubscriptionStatus(_status)

        price = d.pop("price", UNSET)

        provisioning_details = []
        _provisioning_details = d.pop("provisioningDetails", UNSET)
        for provisioning_details_item_data in _provisioning_details or []:
            provisioning_details_item = ProvisioningDetail.from_dict(provisioning_details_item_data)

            provisioning_details.append(provisioning_details_item)

        _commitment_term = d.pop("commitmentTerm", UNSET)
        commitment_term: Union[Unset, SubscriptionCommitment]
        if isinstance(_commitment_term, Unset):
            commitment_term = UNSET
        else:
            commitment_term = SubscriptionCommitment.from_dict(_commitment_term)

        subscription = cls(
            quantity=quantity,
            start_date=start_date,
            billing_term=billing_term,
            id=id,
            company_id=company_id,
            product_id=product_id,
            end_date=end_date,
            created_date=created_date,
            updated_date=updated_date,
            billing_start=billing_start,
            status=status,
            price=price,
            provisioning_details=provisioning_details,
            commitment_term=commitment_term,
        )

        subscription.additional_properties = d
        return subscription

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
