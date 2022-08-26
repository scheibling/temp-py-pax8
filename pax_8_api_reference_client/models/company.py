from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.address import Address
from ..models.company_status import CompanyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Company")


@attr.s(auto_attribs=True)
class Company:
    """
    Attributes:
        name (str): The company name Example: Pax8.
        address (Address):
        phone (str): The primary phone number of the company Example: 555-555-5555.
        website (str): The full URL of the company website Example: https://www.pax8.com/.
        bill_on_behalf_of_enabled (bool): Value is ```true``` if Pax8 handles billing transactions, value is ```false```
            if partner handles billing transactions
        self_service_allowed (bool): Value is ```true``` if self-service privileges are available to the company,
            otherwise value is ```false```
        order_approval_required (bool): Value is ```true``` if the company's self-service orders require approval,
            otherwise value is ```false```
        id (Union[Unset, str]): The unique id of the company
        external_id (Union[Unset, str]): An external ID that can be assigned to the company for reference
        status (Union[Unset, CompanyStatus]): Company Status:
              * `Active` - The company is active
              * `Inactive` - The company is inactive due to missing contacts
              * `Deleted` - The company has been deleted
    """

    name: str
    address: Address
    phone: str
    website: str
    bill_on_behalf_of_enabled: bool
    self_service_allowed: bool
    order_approval_required: bool
    id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    status: Union[Unset, CompanyStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address = self.address.to_dict()

        phone = self.phone
        website = self.website
        bill_on_behalf_of_enabled = self.bill_on_behalf_of_enabled
        self_service_allowed = self.self_service_allowed
        order_approval_required = self.order_approval_required
        id = self.id
        external_id = self.external_id
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "address": address,
                "phone": phone,
                "website": website,
                "billOnBehalfOfEnabled": bill_on_behalf_of_enabled,
                "selfServiceAllowed": self_service_allowed,
                "orderApprovalRequired": order_approval_required,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        address = Address.from_dict(d.pop("address"))

        phone = d.pop("phone")

        website = d.pop("website")

        bill_on_behalf_of_enabled = d.pop("billOnBehalfOfEnabled")

        self_service_allowed = d.pop("selfServiceAllowed")

        order_approval_required = d.pop("orderApprovalRequired")

        id = d.pop("id", UNSET)

        external_id = d.pop("externalId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CompanyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CompanyStatus(_status)

        company = cls(
            name=name,
            address=address,
            phone=phone,
            website=website,
            bill_on_behalf_of_enabled=bill_on_behalf_of_enabled,
            self_service_allowed=self_service_allowed,
            order_approval_required=order_approval_required,
            id=id,
            external_id=external_id,
            status=status,
        )

        company.additional_properties = d
        return company

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
