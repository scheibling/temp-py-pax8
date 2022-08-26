from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageLine")


@attr.s(auto_attribs=True)
class UsageLine:
    """
    Attributes:
        usage_summary_id (Union[Unset, str]): The associated usage summary id
        usage_date (Union[Unset, str]): The date the usage was recorded
        product_name (Union[Unset, str]): The usage product name
        product_id (Union[Unset, str]): The usage product id
        unit_of_measure (Union[Unset, str]): The product unit of measure
        quantity (Union[Unset, float]): The usage quantity
        current_charges (Union[Unset, float]): Charges for the usage line
        current_profit (Union[Unset, float]): Profit for the usage line
        partner_total (Union[Unset, float]): The partner total for the usage line
        unit_price (Union[Unset, float]): The unit price of the usage product
        is_trial (Union[Unset, bool]): Indicates if the usage line is for a trial
    """

    usage_summary_id: Union[Unset, str] = UNSET
    usage_date: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    unit_of_measure: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    current_charges: Union[Unset, float] = UNSET
    current_profit: Union[Unset, float] = UNSET
    partner_total: Union[Unset, float] = UNSET
    unit_price: Union[Unset, float] = UNSET
    is_trial: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        usage_summary_id = self.usage_summary_id
        usage_date = self.usage_date
        product_name = self.product_name
        product_id = self.product_id
        unit_of_measure = self.unit_of_measure
        quantity = self.quantity
        current_charges = self.current_charges
        current_profit = self.current_profit
        partner_total = self.partner_total
        unit_price = self.unit_price
        is_trial = self.is_trial

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if usage_summary_id is not UNSET:
            field_dict["usageSummaryId"] = usage_summary_id
        if usage_date is not UNSET:
            field_dict["usageDate"] = usage_date
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if current_charges is not UNSET:
            field_dict["currentCharges"] = current_charges
        if current_profit is not UNSET:
            field_dict["currentProfit"] = current_profit
        if partner_total is not UNSET:
            field_dict["partnerTotal"] = partner_total
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if is_trial is not UNSET:
            field_dict["isTrial"] = is_trial

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        usage_summary_id = d.pop("usageSummaryId", UNSET)

        usage_date = d.pop("usageDate", UNSET)

        product_name = d.pop("productName", UNSET)

        product_id = d.pop("productId", UNSET)

        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        quantity = d.pop("quantity", UNSET)

        current_charges = d.pop("currentCharges", UNSET)

        current_profit = d.pop("currentProfit", UNSET)

        partner_total = d.pop("partnerTotal", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        is_trial = d.pop("isTrial", UNSET)

        usage_line = cls(
            usage_summary_id=usage_summary_id,
            usage_date=usage_date,
            product_name=product_name,
            product_id=product_id,
            unit_of_measure=unit_of_measure,
            quantity=quantity,
            current_charges=current_charges,
            current_profit=current_profit,
            partner_total=partner_total,
            unit_price=unit_price,
            is_trial=is_trial,
        )

        usage_line.additional_properties = d
        return usage_line

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
