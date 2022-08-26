from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.find_companies_response_200 import FindCompaniesResponse200
from ...models.find_companies_sort import FindCompaniesSort
from ...models.find_companies_status import FindCompaniesStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindCompaniesSort] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    country: Union[Unset, None, str] = UNSET,
    state_or_province: Union[Unset, None, str] = UNSET,
    postal_code: Union[Unset, None, str] = UNSET,
    self_service_allowed: Union[Unset, None, bool] = UNSET,
    bill_on_behalf_of_enabled: Union[Unset, None, bool] = UNSET,
    order_approval_required: Union[Unset, None, bool] = UNSET,
    status: Union[Unset, None, FindCompaniesStatus] = UNSET,
) -> Dict[str, Any]:
    url = "{}/companies".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["size"] = size

    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    params["city"] = city

    params["country"] = country

    params["stateOrProvince"] = state_or_province

    params["postalCode"] = postal_code

    params["selfServiceAllowed"] = self_service_allowed

    params["billOnBehalfOfEnabled"] = bill_on_behalf_of_enabled

    params["orderApprovalRequired"] = order_approval_required

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[FindCompaniesResponse200]:
    if response.status_code == 200:
        response_200 = FindCompaniesResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[FindCompaniesResponse200]:
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
    sort: Union[Unset, None, FindCompaniesSort] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    country: Union[Unset, None, str] = UNSET,
    state_or_province: Union[Unset, None, str] = UNSET,
    postal_code: Union[Unset, None, str] = UNSET,
    self_service_allowed: Union[Unset, None, bool] = UNSET,
    bill_on_behalf_of_enabled: Union[Unset, None, bool] = UNSET,
    order_approval_required: Union[Unset, None, bool] = UNSET,
    status: Union[Unset, None, FindCompaniesStatus] = UNSET,
) -> Response[FindCompaniesResponse200]:
    """Fetch a paginated list of your companies

     Returns a paginated list of all your companies filtered by optional parameters

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindCompaniesSort]):
        city (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        state_or_province (Union[Unset, None, str]):
        postal_code (Union[Unset, None, str]):
        self_service_allowed (Union[Unset, None, bool]):
        bill_on_behalf_of_enabled (Union[Unset, None, bool]):
        order_approval_required (Union[Unset, None, bool]):
        status (Union[Unset, None, FindCompaniesStatus]):

    Returns:
        Response[FindCompaniesResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        size=size,
        sort=sort,
        city=city,
        country=country,
        state_or_province=state_or_province,
        postal_code=postal_code,
        self_service_allowed=self_service_allowed,
        bill_on_behalf_of_enabled=bill_on_behalf_of_enabled,
        order_approval_required=order_approval_required,
        status=status,
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
    sort: Union[Unset, None, FindCompaniesSort] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    country: Union[Unset, None, str] = UNSET,
    state_or_province: Union[Unset, None, str] = UNSET,
    postal_code: Union[Unset, None, str] = UNSET,
    self_service_allowed: Union[Unset, None, bool] = UNSET,
    bill_on_behalf_of_enabled: Union[Unset, None, bool] = UNSET,
    order_approval_required: Union[Unset, None, bool] = UNSET,
    status: Union[Unset, None, FindCompaniesStatus] = UNSET,
) -> Optional[FindCompaniesResponse200]:
    """Fetch a paginated list of your companies

     Returns a paginated list of all your companies filtered by optional parameters

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindCompaniesSort]):
        city (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        state_or_province (Union[Unset, None, str]):
        postal_code (Union[Unset, None, str]):
        self_service_allowed (Union[Unset, None, bool]):
        bill_on_behalf_of_enabled (Union[Unset, None, bool]):
        order_approval_required (Union[Unset, None, bool]):
        status (Union[Unset, None, FindCompaniesStatus]):

    Returns:
        Response[FindCompaniesResponse200]
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
        sort=sort,
        city=city,
        country=country,
        state_or_province=state_or_province,
        postal_code=postal_code,
        self_service_allowed=self_service_allowed,
        bill_on_behalf_of_enabled=bill_on_behalf_of_enabled,
        order_approval_required=order_approval_required,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindCompaniesSort] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    country: Union[Unset, None, str] = UNSET,
    state_or_province: Union[Unset, None, str] = UNSET,
    postal_code: Union[Unset, None, str] = UNSET,
    self_service_allowed: Union[Unset, None, bool] = UNSET,
    bill_on_behalf_of_enabled: Union[Unset, None, bool] = UNSET,
    order_approval_required: Union[Unset, None, bool] = UNSET,
    status: Union[Unset, None, FindCompaniesStatus] = UNSET,
) -> Response[FindCompaniesResponse200]:
    """Fetch a paginated list of your companies

     Returns a paginated list of all your companies filtered by optional parameters

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindCompaniesSort]):
        city (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        state_or_province (Union[Unset, None, str]):
        postal_code (Union[Unset, None, str]):
        self_service_allowed (Union[Unset, None, bool]):
        bill_on_behalf_of_enabled (Union[Unset, None, bool]):
        order_approval_required (Union[Unset, None, bool]):
        status (Union[Unset, None, FindCompaniesStatus]):

    Returns:
        Response[FindCompaniesResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        size=size,
        sort=sort,
        city=city,
        country=country,
        state_or_province=state_or_province,
        postal_code=postal_code,
        self_service_allowed=self_service_allowed,
        bill_on_behalf_of_enabled=bill_on_behalf_of_enabled,
        order_approval_required=order_approval_required,
        status=status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindCompaniesSort] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    country: Union[Unset, None, str] = UNSET,
    state_or_province: Union[Unset, None, str] = UNSET,
    postal_code: Union[Unset, None, str] = UNSET,
    self_service_allowed: Union[Unset, None, bool] = UNSET,
    bill_on_behalf_of_enabled: Union[Unset, None, bool] = UNSET,
    order_approval_required: Union[Unset, None, bool] = UNSET,
    status: Union[Unset, None, FindCompaniesStatus] = UNSET,
) -> Optional[FindCompaniesResponse200]:
    """Fetch a paginated list of your companies

     Returns a paginated list of all your companies filtered by optional parameters

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindCompaniesSort]):
        city (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        state_or_province (Union[Unset, None, str]):
        postal_code (Union[Unset, None, str]):
        self_service_allowed (Union[Unset, None, bool]):
        bill_on_behalf_of_enabled (Union[Unset, None, bool]):
        order_approval_required (Union[Unset, None, bool]):
        status (Union[Unset, None, FindCompaniesStatus]):

    Returns:
        Response[FindCompaniesResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
            sort=sort,
            city=city,
            country=country,
            state_or_province=state_or_province,
            postal_code=postal_code,
            self_service_allowed=self_service_allowed,
            bill_on_behalf_of_enabled=bill_on_behalf_of_enabled,
            order_approval_required=order_approval_required,
            status=status,
        )
    ).parsed
