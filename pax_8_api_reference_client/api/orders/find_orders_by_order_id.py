from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.order import Order
from ...types import Response


def _get_kwargs(
    order_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/orders/{orderId}".format(client.base_url, orderId=order_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, Order]]:
    if response.status_code == 200:
        response_200 = Order.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, Order]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    order_id: str,
    *,
    client: Client,
) -> Response[Union[Error, Order]]:
    """Fetch order details by orderId

     Returns the Order record specified by OrderId

    Args:
        order_id (str):

    Returns:
        Response[Union[Error, Order]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    order_id: str,
    *,
    client: Client,
) -> Optional[Union[Error, Order]]:
    """Fetch order details by orderId

     Returns the Order record specified by OrderId

    Args:
        order_id (str):

    Returns:
        Response[Union[Error, Order]]
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: Client,
) -> Response[Union[Error, Order]]:
    """Fetch order details by orderId

     Returns the Order record specified by OrderId

    Args:
        order_id (str):

    Returns:
        Response[Union[Error, Order]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    order_id: str,
    *,
    client: Client,
) -> Optional[Union[Error, Order]]:
    """Fetch order details by orderId

     Returns the Order record specified by OrderId

    Args:
        order_id (str):

    Returns:
        Response[Union[Error, Order]]
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
        )
    ).parsed
