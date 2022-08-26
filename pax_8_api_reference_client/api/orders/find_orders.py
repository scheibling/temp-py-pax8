from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.find_orders_response_200 import FindOrdersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    company_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/orders".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["size"] = size

    params["companyId"] = company_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, FindOrdersResponse200]]:
    if response.status_code == 200:
        response_200 = FindOrdersResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, FindOrdersResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    company_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, FindOrdersResponse200]]:
    """Fetch a paginated list of orders associated with your partner

     Returns a paginated list of orders

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindOrdersResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        size=size,
        company_id=company_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    company_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, FindOrdersResponse200]]:
    """Fetch a paginated list of orders associated with your partner

     Returns a paginated list of orders

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindOrdersResponse200]]
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
        company_id=company_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    company_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, FindOrdersResponse200]]:
    """Fetch a paginated list of orders associated with your partner

     Returns a paginated list of orders

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindOrdersResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        size=size,
        company_id=company_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    company_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, FindOrdersResponse200]]:
    """Fetch a paginated list of orders associated with your partner

     Returns a paginated list of orders

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindOrdersResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
            company_id=company_id,
        )
    ).parsed
