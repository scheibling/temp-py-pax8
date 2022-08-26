from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.dependencies import Dependencies
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    product_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/products/{productId}/dependencies".format(client.base_url, productId=product_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Dependencies, Error]]:
    if response.status_code == 200:
        response_200 = Dependencies.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Dependencies, Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    product_id: str,
    *,
    client: Client,
) -> Response[Union[Dependencies, Error]]:
    """Fetch a list of product dependencies for a specified product

     Returns associated dependencies for the specified ```productId```. A products dependencies are
    dynamic data.

    Args:
        product_id (str):

    Returns:
        Response[Union[Dependencies, Error]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    product_id: str,
    *,
    client: Client,
) -> Optional[Union[Dependencies, Error]]:
    """Fetch a list of product dependencies for a specified product

     Returns associated dependencies for the specified ```productId```. A products dependencies are
    dynamic data.

    Args:
        product_id (str):

    Returns:
        Response[Union[Dependencies, Error]]
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    product_id: str,
    *,
    client: Client,
) -> Response[Union[Dependencies, Error]]:
    """Fetch a list of product dependencies for a specified product

     Returns associated dependencies for the specified ```productId```. A products dependencies are
    dynamic data.

    Args:
        product_id (str):

    Returns:
        Response[Union[Dependencies, Error]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    product_id: str,
    *,
    client: Client,
) -> Optional[Union[Dependencies, Error]]:
    """Fetch a list of product dependencies for a specified product

     Returns associated dependencies for the specified ```productId```. A products dependencies are
    dynamic data.

    Args:
        product_id (str):

    Returns:
        Response[Union[Dependencies, Error]]
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
        )
    ).parsed
