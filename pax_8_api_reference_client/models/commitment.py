from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Commitment")


@attr.s(auto_attribs=True)
class Commitment:
    """
    Attributes:
        id (Union[Unset, str]): Unique identifier for the commitment record
        term (Union[Unset, str]): Duration of the commitment Example: 3-Year.
        auto_renew (Union[Unset, bool]): Renews without manual intervention at the end of the term
        renewal_window_days_before_term_end (Union[Unset, float]): Number of days _before_ term end-date when renewal
            window opens
        renewal_window_days_after_term_end (Union[Unset, float]): Number of days after the term end-date that renewal
            window closes
        allow_for_quantity_increase (Union[Unset, bool]): Is ```true``` if quantity can be increased during commitment
            term
        allow_for_quantity_decrease (Union[Unset, bool]): Is ```true``` if quantity can be decreased during commitment
            term
        allow_for_early_cancellation (Union[Unset, bool]): Is ```true``` if commitment can be cancelled prior to end of
            term
        cancellation_fee_applied (Union[Unset, bool]): Is ```true``` if canceling subscription entails a fee
        is_transferable (Union[Unset, bool]): Is ```true``` if commitment can be transferred to another company
    """

    id: Union[Unset, str] = UNSET
    term: Union[Unset, str] = UNSET
    auto_renew: Union[Unset, bool] = UNSET
    renewal_window_days_before_term_end: Union[Unset, float] = UNSET
    renewal_window_days_after_term_end: Union[Unset, float] = UNSET
    allow_for_quantity_increase: Union[Unset, bool] = UNSET
    allow_for_quantity_decrease: Union[Unset, bool] = UNSET
    allow_for_early_cancellation: Union[Unset, bool] = UNSET
    cancellation_fee_applied: Union[Unset, bool] = UNSET
    is_transferable: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        term = self.term
        auto_renew = self.auto_renew
        renewal_window_days_before_term_end = self.renewal_window_days_before_term_end
        renewal_window_days_after_term_end = self.renewal_window_days_after_term_end
        allow_for_quantity_increase = self.allow_for_quantity_increase
        allow_for_quantity_decrease = self.allow_for_quantity_decrease
        allow_for_early_cancellation = self.allow_for_early_cancellation
        cancellation_fee_applied = self.cancellation_fee_applied
        is_transferable = self.is_transferable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if term is not UNSET:
            field_dict["term"] = term
        if auto_renew is not UNSET:
            field_dict["autoRenew"] = auto_renew
        if renewal_window_days_before_term_end is not UNSET:
            field_dict["renewalWindowDaysBeforeTermEnd"] = renewal_window_days_before_term_end
        if renewal_window_days_after_term_end is not UNSET:
            field_dict["renewalWindowDaysAfterTermEnd"] = renewal_window_days_after_term_end
        if allow_for_quantity_increase is not UNSET:
            field_dict["allowForQuantityIncrease"] = allow_for_quantity_increase
        if allow_for_quantity_decrease is not UNSET:
            field_dict["allowForQuantityDecrease"] = allow_for_quantity_decrease
        if allow_for_early_cancellation is not UNSET:
            field_dict["allowForEarlyCancellation"] = allow_for_early_cancellation
        if cancellation_fee_applied is not UNSET:
            field_dict["cancellationFeeApplied"] = cancellation_fee_applied
        if is_transferable is not UNSET:
            field_dict["isTransferable"] = is_transferable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        term = d.pop("term", UNSET)

        auto_renew = d.pop("autoRenew", UNSET)

        renewal_window_days_before_term_end = d.pop("renewalWindowDaysBeforeTermEnd", UNSET)

        renewal_window_days_after_term_end = d.pop("renewalWindowDaysAfterTermEnd", UNSET)

        allow_for_quantity_increase = d.pop("allowForQuantityIncrease", UNSET)

        allow_for_quantity_decrease = d.pop("allowForQuantityDecrease", UNSET)

        allow_for_early_cancellation = d.pop("allowForEarlyCancellation", UNSET)

        cancellation_fee_applied = d.pop("cancellationFeeApplied", UNSET)

        is_transferable = d.pop("isTransferable", UNSET)

        commitment = cls(
            id=id,
            term=term,
            auto_renew=auto_renew,
            renewal_window_days_before_term_end=renewal_window_days_before_term_end,
            renewal_window_days_after_term_end=renewal_window_days_after_term_end,
            allow_for_quantity_increase=allow_for_quantity_increase,
            allow_for_quantity_decrease=allow_for_quantity_decrease,
            allow_for_early_cancellation=allow_for_early_cancellation,
            cancellation_fee_applied=cancellation_fee_applied,
            is_transferable=is_transferable,
        )

        commitment.additional_properties = d
        return commitment

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
