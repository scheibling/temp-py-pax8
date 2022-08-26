from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.company import Company
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Company,
) -> Dict[str, Any]:
    url = "{}/companies".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Company, Error]]:
    if response.status_code == 200:
        response_200 = Company.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Company, Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Company,
) -> Response[Union[Company, Error]]:
    """Create a new Company

     Creates a new Company. The Company will be placed in an inactive status until the Company has
    primary Contacts added

    Args:
        json_body (Company):

    Returns:
        Response[Union[Company, Error]]
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
    client: Client,
    json_body: Company,
) -> Optional[Union[Company, Error]]:
    """Create a new Company

     Creates a new Company. The Company will be placed in an inactive status until the Company has
    primary Contacts added

    Args:
        json_body (Company):

    Returns:
        Response[Union[Company, Error]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Company,
) -> Response[Union[Company, Error]]:
    """Create a new Company

     Creates a new Company. The Company will be placed in an inactive status until the Company has
    primary Contacts added

    Args:
        json_body (Company):

    Returns:
        Response[Union[Company, Error]]
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
    client: Client,
    json_body: Company,
) -> Optional[Union[Company, Error]]:
    """Create a new Company

     Creates a new Company. The Company will be placed in an inactive status until the Company has
    primary Contacts added

    Args:
        json_body (Company):

    Returns:
        Response[Union[Company, Error]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
