from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.find_usage_lines_response_200 import FindUsageLinesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    usage_summary_id: str,
    *,
    client: Client,
    usage_date: str,
    product_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/usage-summaries/{usageSummaryId}/usage-lines".format(client.base_url, usageSummaryId=usage_summary_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["usageDate"] = usage_date

    params["productId"] = product_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, FindUsageLinesResponse200]]:
    if response.status_code == 200:
        response_200 = FindUsageLinesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, FindUsageLinesResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    usage_summary_id: str,
    *,
    client: Client,
    usage_date: str,
    product_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, FindUsageLinesResponse200]]:
    """Fetch a paginated list of usage lines for a usage summary

     Fetch a paginated list of usage lines. Default page is 0 and default size is 10. The maximum page
    size is 200

    Args:
        usage_summary_id (str):
        usage_date (str):
        product_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindUsageLinesResponse200]]
    """

    kwargs = _get_kwargs(
        usage_summary_id=usage_summary_id,
        client=client,
        usage_date=usage_date,
        product_id=product_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    usage_summary_id: str,
    *,
    client: Client,
    usage_date: str,
    product_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, FindUsageLinesResponse200]]:
    """Fetch a paginated list of usage lines for a usage summary

     Fetch a paginated list of usage lines. Default page is 0 and default size is 10. The maximum page
    size is 200

    Args:
        usage_summary_id (str):
        usage_date (str):
        product_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindUsageLinesResponse200]]
    """

    return sync_detailed(
        usage_summary_id=usage_summary_id,
        client=client,
        usage_date=usage_date,
        product_id=product_id,
    ).parsed


async def asyncio_detailed(
    usage_summary_id: str,
    *,
    client: Client,
    usage_date: str,
    product_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, FindUsageLinesResponse200]]:
    """Fetch a paginated list of usage lines for a usage summary

     Fetch a paginated list of usage lines. Default page is 0 and default size is 10. The maximum page
    size is 200

    Args:
        usage_summary_id (str):
        usage_date (str):
        product_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindUsageLinesResponse200]]
    """

    kwargs = _get_kwargs(
        usage_summary_id=usage_summary_id,
        client=client,
        usage_date=usage_date,
        product_id=product_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    usage_summary_id: str,
    *,
    client: Client,
    usage_date: str,
    product_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, FindUsageLinesResponse200]]:
    """Fetch a paginated list of usage lines for a usage summary

     Fetch a paginated list of usage lines. Default page is 0 and default size is 10. The maximum page
    size is 200

    Args:
        usage_summary_id (str):
        usage_date (str):
        product_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindUsageLinesResponse200]]
    """

    return (
        await asyncio_detailed(
            usage_summary_id=usage_summary_id,
            client=client,
            usage_date=usage_date,
            product_id=product_id,
        )
    ).parsed
