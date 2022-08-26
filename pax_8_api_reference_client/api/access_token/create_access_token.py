from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.token_request import TokenRequest
from ...models.token_response import TokenResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: TokenRequest,
) -> Dict[str, Any]:
    url = "{}/oauth/token".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, TokenResponse]]:
    if response.status_code == 200:
        response_200 = TokenResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, TokenResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: TokenRequest,
) -> Response[Union[Error, TokenResponse]]:
    """Create a new Access Token

     Create a new Access Token

    Args:
        json_body (TokenRequest):

    Returns:
        Response[Union[Error, TokenResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: TokenRequest,
) -> Optional[Union[Error, TokenResponse]]:
    """Create a new Access Token

     Create a new Access Token

    Args:
        json_body (TokenRequest):

    Returns:
        Response[Union[Error, TokenResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: TokenRequest,
) -> Response[Union[Error, TokenResponse]]:
    """Create a new Access Token

     Create a new Access Token

    Args:
        json_body (TokenRequest):

    Returns:
        Response[Union[Error, TokenResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: TokenRequest,
) -> Optional[Union[Error, TokenResponse]]:
    """Create a new Access Token

     Create a new Access Token

    Args:
        json_body (TokenRequest):

    Returns:
        Response[Union[Error, TokenResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
