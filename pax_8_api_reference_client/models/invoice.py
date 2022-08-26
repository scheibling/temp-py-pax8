from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Invoice")


@attr.s(auto_attribs=True)
class Invoice:
    """
    Attributes:
        id (Union[Unset, str]): The id
        invoice_date (Union[Unset, str]): The date the invoice is generated for
        due_date (Union[Unset, str]): The date on which payment is due
        balance (Union[Unset, float]): The current invoice balance
        carried_balance (Union[Unset, float]): The outstanding balance until current invoiceDate
        total (Union[Unset, float]): The total amount due
        partner_name (Union[Unset, str]): The name of the invoiced partner
        company_id (Union[Unset, str]): The company id
        external_id (Union[Unset, str]): The company external id
    """

    id: Union[Unset, str] = UNSET
    invoice_date: Union[Unset, str] = UNSET
    due_date: Union[Unset, str] = UNSET
    balance: Union[Unset, float] = UNSET
    carried_balance: Union[Unset, float] = UNSET
    total: Union[Unset, float] = UNSET
    partner_name: Union[Unset, str] = UNSET
    company_id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        invoice_date = self.invoice_date
        due_date = self.due_date
        balance = self.balance
        carried_balance = self.carried_balance
        total = self.total
        partner_name = self.partner_name
        company_id = self.company_id
        external_id = self.external_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_date is not UNSET:
            field_dict["invoiceDate"] = invoice_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if balance is not UNSET:
            field_dict["balance"] = balance
        if carried_balance is not UNSET:
            field_dict["carriedBalance"] = carried_balance
        if total is not UNSET:
            field_dict["total"] = total
        if partner_name is not UNSET:
            field_dict["partnerName"] = partner_name
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        invoice_date = d.pop("invoiceDate", UNSET)

        due_date = d.pop("dueDate", UNSET)

        balance = d.pop("balance", UNSET)

        carried_balance = d.pop("carriedBalance", UNSET)

        total = d.pop("total", UNSET)

        partner_name = d.pop("partnerName", UNSET)

        company_id = d.pop("companyId", UNSET)

        external_id = d.pop("externalId", UNSET)

        invoice = cls(
            id=id,
            invoice_date=invoice_date,
            due_date=due_date,
            balance=balance,
            carried_balance=carried_balance,
            total=total,
            partner_name=partner_name,
            company_id=company_id,
            external_id=external_id,
        )

        invoice.additional_properties = d
        return invoice

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
