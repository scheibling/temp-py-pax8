from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.find_subscription_history_by_subscription_id_response_200 import (
    FindSubscriptionHistoryBySubscriptionIdResponse200,
)
from ...types import Response


def _get_kwargs(
    subscription_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/subscriptions/{subscriptionId}/history".format(client.base_url, subscriptionId=subscription_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Error, FindSubscriptionHistoryBySubscriptionIdResponse200]]:
    if response.status_code == 200:
        response_200 = FindSubscriptionHistoryBySubscriptionIdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Error, FindSubscriptionHistoryBySubscriptionIdResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    subscription_id: str,
    *,
    client: Client,
) -> Response[Union[Error, FindSubscriptionHistoryBySubscriptionIdResponse200]]:
    """Fetch the history of a subscription

     Returns a list of changes for a subscription

    Args:
        subscription_id (str):

    Returns:
        Response[Union[Error, FindSubscriptionHistoryBySubscriptionIdResponse200]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    subscription_id: str,
    *,
    client: Client,
) -> Optional[Union[Error, FindSubscriptionHistoryBySubscriptionIdResponse200]]:
    """Fetch the history of a subscription

     Returns a list of changes for a subscription

    Args:
        subscription_id (str):

    Returns:
        Response[Union[Error, FindSubscriptionHistoryBySubscriptionIdResponse200]]
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: Client,
) -> Response[Union[Error, FindSubscriptionHistoryBySubscriptionIdResponse200]]:
    """Fetch the history of a subscription

     Returns a list of changes for a subscription

    Args:
        subscription_id (str):

    Returns:
        Response[Union[Error, FindSubscriptionHistoryBySubscriptionIdResponse200]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: Client,
) -> Optional[Union[Error, FindSubscriptionHistoryBySubscriptionIdResponse200]]:
    """Fetch the history of a subscription

     Returns a list of changes for a subscription

    Args:
        subscription_id (str):

    Returns:
        Response[Union[Error, FindSubscriptionHistoryBySubscriptionIdResponse200]]
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
