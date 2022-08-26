from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.find_all_products_response_200 import FindAllProductsResponse200
from ...models.find_all_products_sort import FindAllProductsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindAllProductsSort] = UNSET,
    vendor_name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/products".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["size"] = size

    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    params["vendorName"] = vendor_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[FindAllProductsResponse200]:
    if response.status_code == 200:
        response_200 = FindAllProductsResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[FindAllProductsResponse200]:
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
    sort: Union[Unset, None, FindAllProductsSort] = UNSET,
    vendor_name: Union[Unset, None, str] = UNSET,
) -> Response[FindAllProductsResponse200]:
    """Fetch a paginated list of Pax8 products

     Returns a paginated list of Pax8 products filtered by optional query parameters

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindAllProductsSort]):
        vendor_name (Union[Unset, None, str]):

    Returns:
        Response[FindAllProductsResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        size=size,
        sort=sort,
        vendor_name=vendor_name,
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
    sort: Union[Unset, None, FindAllProductsSort] = UNSET,
    vendor_name: Union[Unset, None, str] = UNSET,
) -> Optional[FindAllProductsResponse200]:
    """Fetch a paginated list of Pax8 products

     Returns a paginated list of Pax8 products filtered by optional query parameters

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindAllProductsSort]):
        vendor_name (Union[Unset, None, str]):

    Returns:
        Response[FindAllProductsResponse200]
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
        sort=sort,
        vendor_name=vendor_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindAllProductsSort] = UNSET,
    vendor_name: Union[Unset, None, str] = UNSET,
) -> Response[FindAllProductsResponse200]:
    """Fetch a paginated list of Pax8 products

     Returns a paginated list of Pax8 products filtered by optional query parameters

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindAllProductsSort]):
        vendor_name (Union[Unset, None, str]):

    Returns:
        Response[FindAllProductsResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        size=size,
        sort=sort,
        vendor_name=vendor_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindAllProductsSort] = UNSET,
    vendor_name: Union[Unset, None, str] = UNSET,
) -> Optional[FindAllProductsResponse200]:
    """Fetch a paginated list of Pax8 products

     Returns a paginated list of Pax8 products filtered by optional query parameters

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindAllProductsSort]):
        vendor_name (Union[Unset, None, str]):

    Returns:
        Response[FindAllProductsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
            sort=sort,
            vendor_name=vendor_name,
        )
    ).parsed
