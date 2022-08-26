from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.order import Order
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: Order,
    is_mock: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/orders".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["isMock"] = is_mock

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, Order]]:
    if response.status_code == 200:
        response_200 = Order.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, Order]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Order,
    is_mock: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Error, Order]]:
    """Create a new order for a specified company

    Args:
        is_mock (Union[Unset, None, bool]):
        json_body (Order):

    Returns:
        Response[Union[Error, Order]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        is_mock=is_mock,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: Order,
    is_mock: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Error, Order]]:
    """Create a new order for a specified company

    Args:
        is_mock (Union[Unset, None, bool]):
        json_body (Order):

    Returns:
        Response[Union[Error, Order]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        is_mock=is_mock,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Order,
    is_mock: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Error, Order]]:
    """Create a new order for a specified company

    Args:
        is_mock (Union[Unset, None, bool]):
        json_body (Order):

    Returns:
        Response[Union[Error, Order]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        is_mock=is_mock,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: Order,
    is_mock: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Error, Order]]:
    """Create a new order for a specified company

    Args:
        is_mock (Union[Unset, None, bool]):
        json_body (Order):

    Returns:
        Response[Union[Error, Order]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            is_mock=is_mock,
        )
    ).parsed
