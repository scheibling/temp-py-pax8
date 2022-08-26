from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageSummary")


@attr.s(auto_attribs=True)
class UsageSummary:
    """
    Attributes:
        id (Union[Unset, str]): The id
        company_id (Union[Unset, str]): The company id
        product_id (Union[Unset, str]): The product id
        resource_group (Union[Unset, str]): Resource group assigned to the usage summary
        vendor_name (Union[Unset, str]): Vendor Name
        current_charges (Union[Unset, float]): Charges for the current month
        partner_total (Union[Unset, float]): The partner total for the current month
        is_trial (Union[Unset, bool]): Indicates whether the usage summary is for a trial
    """

    id: Union[Unset, str] = UNSET
    company_id: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    resource_group: Union[Unset, str] = UNSET
    vendor_name: Union[Unset, str] = UNSET
    current_charges: Union[Unset, float] = UNSET
    partner_total: Union[Unset, float] = UNSET
    is_trial: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        company_id = self.company_id
        product_id = self.product_id
        resource_group = self.resource_group
        vendor_name = self.vendor_name
        current_charges = self.current_charges
        partner_total = self.partner_total
        is_trial = self.is_trial

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if vendor_name is not UNSET:
            field_dict["vendorName"] = vendor_name
        if current_charges is not UNSET:
            field_dict["currentCharges"] = current_charges
        if partner_total is not UNSET:
            field_dict["partnerTotal"] = partner_total
        if is_trial is not UNSET:
            field_dict["isTrial"] = is_trial

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        product_id = d.pop("productId", UNSET)

        resource_group = d.pop("resourceGroup", UNSET)

        vendor_name = d.pop("vendorName", UNSET)

        current_charges = d.pop("currentCharges", UNSET)

        partner_total = d.pop("partnerTotal", UNSET)

        is_trial = d.pop("isTrial", UNSET)

        usage_summary = cls(
            id=id,
            company_id=company_id,
            product_id=product_id,
            resource_group=resource_group,
            vendor_name=vendor_name,
            current_charges=current_charges,
            partner_total=partner_total,
            is_trial=is_trial,
        )

        usage_summary.additional_properties = d
        return usage_summary

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
