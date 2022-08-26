from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.token_response_expires_in import TokenResponseExpiresIn
from ..models.token_response_token_type import TokenResponseTokenType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenResponse")


@attr.s(auto_attribs=True)
class TokenResponse:
    """
    Attributes:
        access_token (Union[Unset, str]): The Access Token
        expires_in (Union[Unset, TokenResponseExpiresIn]): The time to live of the Access Token in seconds
        token_type (Union[Unset, TokenResponseTokenType]):
    """

    access_token: Union[Unset, str] = UNSET
    expires_in: Union[Unset, TokenResponseExpiresIn] = UNSET
    token_type: Union[Unset, TokenResponseTokenType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token
        expires_in: Union[Unset, int] = UNSET
        if not isinstance(self.expires_in, Unset):
            expires_in = self.expires_in.value

        token_type: Union[Unset, str] = UNSET
        if not isinstance(self.token_type, Unset):
            token_type = self.token_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if token_type is not UNSET:
            field_dict["token_type"] = token_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("access_token", UNSET)

        _expires_in = d.pop("expires_in", UNSET)
        expires_in: Union[Unset, TokenResponseExpiresIn]
        if isinstance(_expires_in, Unset):
            expires_in = UNSET
        else:
            expires_in = TokenResponseExpiresIn(_expires_in)

        _token_type = d.pop("token_type", UNSET)
        token_type: Union[Unset, TokenResponseTokenType]
        if isinstance(_token_type, Unset):
            token_type = UNSET
        else:
            token_type = TokenResponseTokenType(_token_type)

        token_response = cls(
            access_token=access_token,
            expires_in=expires_in,
            token_type=token_type,
        )

        token_response.additional_properties = d
        return token_response

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
