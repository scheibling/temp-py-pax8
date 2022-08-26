from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.subscription import Subscription
from ...types import Response


def _get_kwargs(
    subscription_id: str,
    *,
    client: Client,
    json_body: Subscription,
) -> Dict[str, Any]:
    url = "{}/subscriptions/{subscriptionId}".format(client.base_url, subscriptionId=subscription_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, Subscription]]:
    if response.status_code == 200:
        response_200 = Subscription.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, Subscription]]:
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
    json_body: Subscription,
) -> Response[Union[Error, Subscription]]:
    """Update a specified subscription

     Updates a subscription

    Args:
        subscription_id (str):
        json_body (Subscription):

    Returns:
        Response[Union[Error, Subscription]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        client=client,
        json_body=json_body,
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
    json_body: Subscription,
) -> Optional[Union[Error, Subscription]]:
    """Update a specified subscription

     Updates a subscription

    Args:
        subscription_id (str):
        json_body (Subscription):

    Returns:
        Response[Union[Error, Subscription]]
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: Client,
    json_body: Subscription,
) -> Response[Union[Error, Subscription]]:
    """Update a specified subscription

     Updates a subscription

    Args:
        subscription_id (str):
        json_body (Subscription):

    Returns:
        Response[Union[Error, Subscription]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: Client,
    json_body: Subscription,
) -> Optional[Union[Error, Subscription]]:
    """Update a specified subscription

     Updates a subscription

    Args:
        subscription_id (str):
        json_body (Subscription):

    Returns:
        Response[Union[Error, Subscription]]
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
