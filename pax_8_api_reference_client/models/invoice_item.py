from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.invoice_item_charge_type import InvoiceItemChargeType
from ..models.invoice_item_rate_type import InvoiceItemRateType
from ..models.invoice_item_term import InvoiceItemTerm
from ..models.invoice_item_type import InvoiceItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceItem")


@attr.s(auto_attribs=True)
class InvoiceItem:
    """
    Attributes:
        id (Union[Unset, str]): The unique id for this invoice item
        purchase_order_number (Union[Unset, str]): The purchase order number
        type (Union[Unset, InvoiceItemType]): The item type
        company_id (Union[Unset, str]): The company id
        external_id (Union[Unset, str]): The company external id
        company_name (Union[Unset, str]): The name of the company
        start_period (Union[Unset, str]): The start period
        end_period (Union[Unset, str]): The end period
        quantity (Union[Unset, float]): The quantity of this SKU
        unit_of_measure (Union[Unset, str]): The unit of measure
        term (Union[Unset, InvoiceItemTerm]): The billing term
        sku (Union[Unset, str]): The product sku
        description (Union[Unset, str]): The description
        details (Union[Unset, str]): The details
        rate_type (Union[Unset, InvoiceItemRateType]): The rate type
        charge_type (Union[Unset, InvoiceItemChargeType]): The charge type
        price (Union[Unset, float]): The customer unit price
        sub_total (Union[Unset, float]): The customer sub total. Represents cost of services plus billing fees.
        cost (Union[Unset, float]): The partner unit cost
        cost_total (Union[Unset, float]): The partner total cost of the services
        offered_by (Union[Unset, str]): The account who offers this product
        billed_by_pax_8 (Union[Unset, bool]): Is the item billed directly by Pax8
        total (Union[Unset, float]): The customer total including all services and fees
        product_id (Union[Unset, str]): The product id
        product_name (Union[Unset, str]): The product name
        billing_fee (Union[Unset, float]): The fee for Pax8 billing a bill on behalf of company
        billing_fee_rate (Union[Unset, float]): The fee rate for Pax8 billing a bill on behalf of company
        amount_due (Union[Unset, float]): The final total due for the item for this invoice
        currency_code (Union[Unset, str]): The currency ISO 4217 code
    """

    id: Union[Unset, str] = UNSET
    purchase_order_number: Union[Unset, str] = UNSET
    type: Union[Unset, InvoiceItemType] = UNSET
    company_id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    start_period: Union[Unset, str] = UNSET
    end_period: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    unit_of_measure: Union[Unset, str] = UNSET
    term: Union[Unset, InvoiceItemTerm] = UNSET
    sku: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    rate_type: Union[Unset, InvoiceItemRateType] = UNSET
    charge_type: Union[Unset, InvoiceItemChargeType] = UNSET
    price: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    cost: Union[Unset, float] = UNSET
    cost_total: Union[Unset, float] = UNSET
    offered_by: Union[Unset, str] = UNSET
    billed_by_pax_8: Union[Unset, bool] = UNSET
    total: Union[Unset, float] = UNSET
    product_id: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    billing_fee: Union[Unset, float] = UNSET
    billing_fee_rate: Union[Unset, float] = UNSET
    amount_due: Union[Unset, float] = UNSET
    currency_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        purchase_order_number = self.purchase_order_number
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        company_id = self.company_id
        external_id = self.external_id
        company_name = self.company_name
        start_period = self.start_period
        end_period = self.end_period
        quantity = self.quantity
        unit_of_measure = self.unit_of_measure
        term: Union[Unset, str] = UNSET
        if not isinstance(self.term, Unset):
            term = self.term.value

        sku = self.sku
        description = self.description
        details = self.details
        rate_type: Union[Unset, str] = UNSET
        if not isinstance(self.rate_type, Unset):
            rate_type = self.rate_type.value

        charge_type: Union[Unset, str] = UNSET
        if not isinstance(self.charge_type, Unset):
            charge_type = self.charge_type.value

        price = self.price
        sub_total = self.sub_total
        cost = self.cost
        cost_total = self.cost_total
        offered_by = self.offered_by
        billed_by_pax_8 = self.billed_by_pax_8
        total = self.total
        product_id = self.product_id
        product_name = self.product_name
        billing_fee = self.billing_fee
        billing_fee_rate = self.billing_fee_rate
        amount_due = self.amount_due
        currency_code = self.currency_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if purchase_order_number is not UNSET:
            field_dict["purchaseOrderNumber"] = purchase_order_number
        if type is not UNSET:
            field_dict["type"] = type
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if start_period is not UNSET:
            field_dict["startPeriod"] = start_period
        if end_period is not UNSET:
            field_dict["endPeriod"] = end_period
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure
        if term is not UNSET:
            field_dict["term"] = term
        if sku is not UNSET:
            field_dict["sku"] = sku
        if description is not UNSET:
            field_dict["description"] = description
        if details is not UNSET:
            field_dict["details"] = details
        if rate_type is not UNSET:
            field_dict["rateType"] = rate_type
        if charge_type is not UNSET:
            field_dict["chargeType"] = charge_type
        if price is not UNSET:
            field_dict["price"] = price
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if cost is not UNSET:
            field_dict["cost"] = cost
        if cost_total is not UNSET:
            field_dict["costTotal"] = cost_total
        if offered_by is not UNSET:
            field_dict["offeredBy"] = offered_by
        if billed_by_pax_8 is not UNSET:
            field_dict["billedByPax8"] = billed_by_pax_8
        if total is not UNSET:
            field_dict["total"] = total
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if billing_fee is not UNSET:
            field_dict["billingFee"] = billing_fee
        if billing_fee_rate is not UNSET:
            field_dict["billingFeeRate"] = billing_fee_rate
        if amount_due is not UNSET:
            field_dict["amountDue"] = amount_due
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        purchase_order_number = d.pop("purchaseOrderNumber", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, InvoiceItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = InvoiceItemType(_type)

        company_id = d.pop("companyId", UNSET)

        external_id = d.pop("externalId", UNSET)

        company_name = d.pop("companyName", UNSET)

        start_period = d.pop("startPeriod", UNSET)

        end_period = d.pop("endPeriod", UNSET)

        quantity = d.pop("quantity", UNSET)

        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        _term = d.pop("term", UNSET)
        term: Union[Unset, InvoiceItemTerm]
        if isinstance(_term, Unset):
            term = UNSET
        else:
            term = InvoiceItemTerm(_term)

        sku = d.pop("sku", UNSET)

        description = d.pop("description", UNSET)

        details = d.pop("details", UNSET)

        _rate_type = d.pop("rateType", UNSET)
        rate_type: Union[Unset, InvoiceItemRateType]
        if isinstance(_rate_type, Unset):
            rate_type = UNSET
        else:
            rate_type = InvoiceItemRateType(_rate_type)

        _charge_type = d.pop("chargeType", UNSET)
        charge_type: Union[Unset, InvoiceItemChargeType]
        if isinstance(_charge_type, Unset):
            charge_type = UNSET
        else:
            charge_type = InvoiceItemChargeType(_charge_type)

        price = d.pop("price", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        cost = d.pop("cost", UNSET)

        cost_total = d.pop("costTotal", UNSET)

        offered_by = d.pop("offeredBy", UNSET)

        billed_by_pax_8 = d.pop("billedByPax8", UNSET)

        total = d.pop("total", UNSET)

        product_id = d.pop("productId", UNSET)

        product_name = d.pop("productName", UNSET)

        billing_fee = d.pop("billingFee", UNSET)

        billing_fee_rate = d.pop("billingFeeRate", UNSET)

        amount_due = d.pop("amountDue", UNSET)

        currency_code = d.pop("currencyCode", UNSET)

        invoice_item = cls(
            id=id,
            purchase_order_number=purchase_order_number,
            type=type,
            company_id=company_id,
            external_id=external_id,
            company_name=company_name,
            start_period=start_period,
            end_period=end_period,
            quantity=quantity,
            unit_of_measure=unit_of_measure,
            term=term,
            sku=sku,
            description=description,
            details=details,
            rate_type=rate_type,
            charge_type=charge_type,
            price=price,
            sub_total=sub_total,
            cost=cost,
            cost_total=cost_total,
            offered_by=offered_by,
            billed_by_pax_8=billed_by_pax_8,
            total=total,
            product_id=product_id,
            product_name=product_name,
            billing_fee=billing_fee,
            billing_fee_rate=billing_fee_rate,
            amount_due=amount_due,
            currency_code=currency_code,
        )

        invoice_item.additional_properties = d
        return invoice_item

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
