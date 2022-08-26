from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.get_companies_company_id_contacts_response_200 import GetCompaniesCompanyIdContactsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
) -> Dict[str, Any]:
    url = "{}/companies/{companyId}/contacts".format(client.base_url, companyId=company_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["size"] = size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, GetCompaniesCompanyIdContactsResponse200]]:
    if response.status_code == 200:
        response_200 = GetCompaniesCompanyIdContactsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, GetCompaniesCompanyIdContactsResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    company_id: str,
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
) -> Response[Union[Error, GetCompaniesCompanyIdContactsResponse200]]:
    """Fetch a paginated list of contacts

     Returns a paginated list of contacts ordered by ```createDate``` descending

    Args:
        company_id (str):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.

    Returns:
        Response[Union[Error, GetCompaniesCompanyIdContactsResponse200]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        page=page,
        size=size,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    company_id: str,
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
) -> Optional[Union[Error, GetCompaniesCompanyIdContactsResponse200]]:
    """Fetch a paginated list of contacts

     Returns a paginated list of contacts ordered by ```createDate``` descending

    Args:
        company_id (str):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.

    Returns:
        Response[Union[Error, GetCompaniesCompanyIdContactsResponse200]]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        page=page,
        size=size,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
) -> Response[Union[Error, GetCompaniesCompanyIdContactsResponse200]]:
    """Fetch a paginated list of contacts

     Returns a paginated list of contacts ordered by ```createDate``` descending

    Args:
        company_id (str):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.

    Returns:
        Response[Union[Error, GetCompaniesCompanyIdContactsResponse200]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        page=page,
        size=size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    company_id: str,
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
) -> Optional[Union[Error, GetCompaniesCompanyIdContactsResponse200]]:
    """Fetch a paginated list of contacts

     Returns a paginated list of contacts ordered by ```createDate``` descending

    Args:
        company_id (str):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.

    Returns:
        Response[Union[Error, GetCompaniesCompanyIdContactsResponse200]]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            page=page,
            size=size,
        )
    ).parsed
