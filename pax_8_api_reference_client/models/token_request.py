from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.token_request_audience import TokenRequestAudience
from ..models.token_request_grant_type import TokenRequestGrantType

T = TypeVar("T", bound="TokenRequest")


@attr.s(auto_attribs=True)
class TokenRequest:
    """
    Attributes:
        client_id (str): The client id
        client_secret (str): The client secret
        audience (TokenRequestAudience):
        grant_type (TokenRequestGrantType):
    """

    client_id: str
    client_secret: str
    audience: TokenRequestAudience
    grant_type: TokenRequestGrantType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id
        client_secret = self.client_secret
        audience = self.audience.value

        grant_type = self.grant_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "client_secret": client_secret,
                "audience": audience,
                "grant_type": grant_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        audience = TokenRequestAudience(d.pop("audience"))

        grant_type = TokenRequestGrantType(d.pop("grant_type"))

        token_request = cls(
            client_id=client_id,
            client_secret=client_secret,
            audience=audience,
            grant_type=grant_type,
        )

        token_request.additional_properties = d
        return token_request

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
