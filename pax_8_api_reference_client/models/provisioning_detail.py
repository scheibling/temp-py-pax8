from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.provisioning_detail_value_type import ProvisioningDetailValueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProvisioningDetail")


@attr.s(auto_attribs=True)
class ProvisioningDetail:
    """
    Attributes:
        label (Union[Unset, str]): The label to display
        key (Union[Unset, str]): The key Example: userEmailAddress.
        values (Union[Unset, List[str]]): A list of values based on the ```valuetype``` and ```possibleValues```
        description (Union[Unset, str]): Instructions and context to help enter the required provisioning information
            Example: Provide the user's email address.
        value_type (Union[Unset, ProvisioningDetailValueType]): Provisioning Detail Value Type:
             * `Input` - A value that is supplied by a user
             * `Single-Value` - A single value that is picked from the `possibleValues` list
             * `Multi-Value` - One or multiple values that are picked from the `possibleValues` list
        possible_values (Union[Unset, List[str]]): A list of possible values. `possibleValues` will be null when
            `valueType` is `Input`
    """

    label: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    values: Union[Unset, List[str]] = UNSET
    description: Union[Unset, str] = UNSET
    value_type: Union[Unset, ProvisioningDetailValueType] = UNSET
    possible_values: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        key = self.key
        values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        description = self.description
        value_type: Union[Unset, str] = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = self.value_type.value

        possible_values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.possible_values, Unset):
            possible_values = self.possible_values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if key is not UNSET:
            field_dict["key"] = key
        if values is not UNSET:
            field_dict["values"] = values
        if description is not UNSET:
            field_dict["description"] = description
        if value_type is not UNSET:
            field_dict["valueType"] = value_type
        if possible_values is not UNSET:
            field_dict["possibleValues"] = possible_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label", UNSET)

        key = d.pop("key", UNSET)

        values = cast(List[str], d.pop("values", UNSET))

        description = d.pop("description", UNSET)

        _value_type = d.pop("valueType", UNSET)
        value_type: Union[Unset, ProvisioningDetailValueType]
        if isinstance(_value_type, Unset):
            value_type = UNSET
        else:
            value_type = ProvisioningDetailValueType(_value_type)

        possible_values = cast(List[str], d.pop("possibleValues", UNSET))

        provisioning_detail = cls(
            label=label,
            key=key,
            values=values,
            description=description,
            value_type=value_type,
            possible_values=possible_values,
        )

        provisioning_detail.additional_properties = d
        return provisioning_detail

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
