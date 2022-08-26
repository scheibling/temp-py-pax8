from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    subscription_id: str,
    *,
    client: Client,
    cancel_date: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/subscriptions/{subscriptionId}".format(client.base_url, subscriptionId=subscription_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["cancelDate"] = cancel_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Error]]:
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
    cancel_date: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, Error]]:
    """Cancel a subscription

     Cancels the Subscription specified by subscriptionId

    Args:
        subscription_id (str):
        cancel_date (Union[Unset, None, str]):  Example: 2021-01-23.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        client=client,
        cancel_date=cancel_date,
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
    cancel_date: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, Error]]:
    """Cancel a subscription

     Cancels the Subscription specified by subscriptionId

    Args:
        subscription_id (str):
        cancel_date (Union[Unset, None, str]):  Example: 2021-01-23.

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
        cancel_date=cancel_date,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: Client,
    cancel_date: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, Error]]:
    """Cancel a subscription

     Cancels the Subscription specified by subscriptionId

    Args:
        subscription_id (str):
        cancel_date (Union[Unset, None, str]):  Example: 2021-01-23.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        client=client,
        cancel_date=cancel_date,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: Client,
    cancel_date: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, Error]]:
    """Cancel a subscription

     Cancels the Subscription specified by subscriptionId

    Args:
        subscription_id (str):
        cancel_date (Union[Unset, None, str]):  Example: 2021-01-23.

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
            cancel_date=cancel_date,
        )
    ).parsed
