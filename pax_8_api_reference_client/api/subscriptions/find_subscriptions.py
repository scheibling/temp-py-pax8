from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.find_subscriptions_billing_term import FindSubscriptionsBillingTerm
from ...models.find_subscriptions_response_200 import FindSubscriptionsResponse200
from ...models.find_subscriptions_sort import FindSubscriptionsSort
from ...models.find_subscriptions_status import FindSubscriptionsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindSubscriptionsSort] = UNSET,
    status: Union[Unset, None, FindSubscriptionsStatus] = UNSET,
    billing_term: Union[Unset, None, FindSubscriptionsBillingTerm] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
    product_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/subscriptions".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["size"] = size

    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    json_billing_term: Union[Unset, None, str] = UNSET
    if not isinstance(billing_term, Unset):
        json_billing_term = billing_term.value if billing_term else None

    params["billingTerm"] = json_billing_term

    params["companyId"] = company_id

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, FindSubscriptionsResponse200]]:
    if response.status_code == 200:
        response_200 = FindSubscriptionsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, FindSubscriptionsResponse200]]:
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
    sort: Union[Unset, None, FindSubscriptionsSort] = UNSET,
    status: Union[Unset, None, FindSubscriptionsStatus] = UNSET,
    billing_term: Union[Unset, None, FindSubscriptionsBillingTerm] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
    product_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, FindSubscriptionsResponse200]]:
    """Fetch a paginated list of subscriptions

     Fetch a paginated list of subscriptions. Default page is 0 and default size is 10. The maximum page
    size is 200

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindSubscriptionsSort]):
        status (Union[Unset, None, FindSubscriptionsStatus]):
        billing_term (Union[Unset, None, FindSubscriptionsBillingTerm]):
        company_id (Union[Unset, None, str]):
        product_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindSubscriptionsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        size=size,
        sort=sort,
        status=status,
        billing_term=billing_term,
        company_id=company_id,
        product_id=product_id,
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
    sort: Union[Unset, None, FindSubscriptionsSort] = UNSET,
    status: Union[Unset, None, FindSubscriptionsStatus] = UNSET,
    billing_term: Union[Unset, None, FindSubscriptionsBillingTerm] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
    product_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, FindSubscriptionsResponse200]]:
    """Fetch a paginated list of subscriptions

     Fetch a paginated list of subscriptions. Default page is 0 and default size is 10. The maximum page
    size is 200

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindSubscriptionsSort]):
        status (Union[Unset, None, FindSubscriptionsStatus]):
        billing_term (Union[Unset, None, FindSubscriptionsBillingTerm]):
        company_id (Union[Unset, None, str]):
        product_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindSubscriptionsResponse200]]
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
        sort=sort,
        status=status,
        billing_term=billing_term,
        company_id=company_id,
        product_id=product_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindSubscriptionsSort] = UNSET,
    status: Union[Unset, None, FindSubscriptionsStatus] = UNSET,
    billing_term: Union[Unset, None, FindSubscriptionsBillingTerm] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
    product_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, FindSubscriptionsResponse200]]:
    """Fetch a paginated list of subscriptions

     Fetch a paginated list of subscriptions. Default page is 0 and default size is 10. The maximum page
    size is 200

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindSubscriptionsSort]):
        status (Union[Unset, None, FindSubscriptionsStatus]):
        billing_term (Union[Unset, None, FindSubscriptionsBillingTerm]):
        company_id (Union[Unset, None, str]):
        product_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindSubscriptionsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        size=size,
        sort=sort,
        status=status,
        billing_term=billing_term,
        company_id=company_id,
        product_id=product_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindSubscriptionsSort] = UNSET,
    status: Union[Unset, None, FindSubscriptionsStatus] = UNSET,
    billing_term: Union[Unset, None, FindSubscriptionsBillingTerm] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
    product_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, FindSubscriptionsResponse200]]:
    """Fetch a paginated list of subscriptions

     Fetch a paginated list of subscriptions. Default page is 0 and default size is 10. The maximum page
    size is 200

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindSubscriptionsSort]):
        status (Union[Unset, None, FindSubscriptionsStatus]):
        billing_term (Union[Unset, None, FindSubscriptionsBillingTerm]):
        company_id (Union[Unset, None, str]):
        product_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindSubscriptionsResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
            sort=sort,
            status=status,
            billing_term=billing_term,
            company_id=company_id,
            product_id=product_id,
        )
    ).parsed
