from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.find_subscription_usage_summaries_response_200 import FindSubscriptionUsageSummariesResponse200
from ...models.find_subscription_usage_summaries_sort import FindSubscriptionUsageSummariesSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    subscription_id: str,
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindSubscriptionUsageSummariesSort] = UNSET,
    resource_group: Union[Unset, None, str] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/subscriptions/{subscriptionId}/usage-summaries".format(client.base_url, subscriptionId=subscription_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["size"] = size

    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    params["resourceGroup"] = resource_group

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, FindSubscriptionUsageSummariesResponse200]]:
    if response.status_code == 200:
        response_200 = FindSubscriptionUsageSummariesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, FindSubscriptionUsageSummariesResponse200]]:
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
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindSubscriptionUsageSummariesSort] = UNSET,
    resource_group: Union[Unset, None, str] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, FindSubscriptionUsageSummariesResponse200]]:
    """Fetch a paginated list of usage summaries

     Fetch a paginated list of usage summaries. Default page is 0 and default size is 10. The maximum
    page size is 200

    Args:
        subscription_id (str):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindSubscriptionUsageSummariesSort]):
        resource_group (Union[Unset, None, str]):
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindSubscriptionUsageSummariesResponse200]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        client=client,
        page=page,
        size=size,
        sort=sort,
        resource_group=resource_group,
        company_id=company_id,
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
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindSubscriptionUsageSummariesSort] = UNSET,
    resource_group: Union[Unset, None, str] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, FindSubscriptionUsageSummariesResponse200]]:
    """Fetch a paginated list of usage summaries

     Fetch a paginated list of usage summaries. Default page is 0 and default size is 10. The maximum
    page size is 200

    Args:
        subscription_id (str):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindSubscriptionUsageSummariesSort]):
        resource_group (Union[Unset, None, str]):
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindSubscriptionUsageSummariesResponse200]]
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
        page=page,
        size=size,
        sort=sort,
        resource_group=resource_group,
        company_id=company_id,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindSubscriptionUsageSummariesSort] = UNSET,
    resource_group: Union[Unset, None, str] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, FindSubscriptionUsageSummariesResponse200]]:
    """Fetch a paginated list of usage summaries

     Fetch a paginated list of usage summaries. Default page is 0 and default size is 10. The maximum
    page size is 200

    Args:
        subscription_id (str):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindSubscriptionUsageSummariesSort]):
        resource_group (Union[Unset, None, str]):
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindSubscriptionUsageSummariesResponse200]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        client=client,
        page=page,
        size=size,
        sort=sort,
        resource_group=resource_group,
        company_id=company_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindSubscriptionUsageSummariesSort] = UNSET,
    resource_group: Union[Unset, None, str] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, FindSubscriptionUsageSummariesResponse200]]:
    """Fetch a paginated list of usage summaries

     Fetch a paginated list of usage summaries. Default page is 0 and default size is 10. The maximum
    page size is 200

    Args:
        subscription_id (str):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindSubscriptionUsageSummariesSort]):
        resource_group (Union[Unset, None, str]):
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindSubscriptionUsageSummariesResponse200]]
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
            page=page,
            size=size,
            sort=sort,
            resource_group=resource_group,
            company_id=company_id,
        )
    ).parsed
