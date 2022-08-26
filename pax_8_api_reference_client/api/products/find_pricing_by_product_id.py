from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.find_pricing_by_product_id_response_200 import FindPricingByProductIdResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_id: str,
    *,
    client: Client,
    company_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/products/{productId}/pricing".format(client.base_url, productId=product_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, FindPricingByProductIdResponse200]]:
    if response.status_code == 200:
        response_200 = FindPricingByProductIdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, FindPricingByProductIdResponse200]]:
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
    company_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, FindPricingByProductIdResponse200]]:
    """Fetch pricing information for a particular product

     Returns recommended pricing and partner cost for the specified productId. A products pricing is
    dynamic data.

    Args:
        product_id (str):
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindPricingByProductIdResponse200]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
        company_id=company_id,
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
    company_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, FindPricingByProductIdResponse200]]:
    """Fetch pricing information for a particular product

     Returns recommended pricing and partner cost for the specified productId. A products pricing is
    dynamic data.

    Args:
        product_id (str):
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindPricingByProductIdResponse200]]
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        company_id=company_id,
    ).parsed


async def asyncio_detailed(
    product_id: str,
    *,
    client: Client,
    company_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, FindPricingByProductIdResponse200]]:
    """Fetch pricing information for a particular product

     Returns recommended pricing and partner cost for the specified productId. A products pricing is
    dynamic data.

    Args:
        product_id (str):
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindPricingByProductIdResponse200]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
        company_id=company_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    product_id: str,
    *,
    client: Client,
    company_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, FindPricingByProductIdResponse200]]:
    """Fetch pricing information for a particular product

     Returns recommended pricing and partner cost for the specified productId. A products pricing is
    dynamic data.

    Args:
        product_id (str):
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindPricingByProductIdResponse200]]
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            company_id=company_id,
        )
    ).parsed
