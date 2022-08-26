from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.find_partner_invoices_response_200 import FindPartnerInvoicesResponse200
from ...models.find_partner_invoices_sort import FindPartnerInvoicesSort
from ...models.find_partner_invoices_status import FindPartnerInvoicesStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindPartnerInvoicesSort] = UNSET,
    status: Union[Unset, None, FindPartnerInvoicesStatus] = UNSET,
    invoice_date: Union[Unset, None, str] = UNSET,
    invoice_date_range_start: Union[Unset, None, str] = UNSET,
    invoice_date_range_end: Union[Unset, None, str] = UNSET,
    due_date: Union[Unset, None, str] = UNSET,
    total: Union[Unset, None, float] = UNSET,
    balance: Union[Unset, None, float] = UNSET,
    carried_balance: Union[Unset, None, float] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/invoices".format(client.base_url)

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

    params["invoiceDate"] = invoice_date

    params["invoiceDateRangeStart"] = invoice_date_range_start

    params["invoiceDateRangeEnd"] = invoice_date_range_end

    params["dueDate"] = due_date

    params["total"] = total

    params["balance"] = balance

    params["carriedBalance"] = carried_balance

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, FindPartnerInvoicesResponse200]]:
    if response.status_code == 200:
        response_200 = FindPartnerInvoicesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, FindPartnerInvoicesResponse200]]:
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
    sort: Union[Unset, None, FindPartnerInvoicesSort] = UNSET,
    status: Union[Unset, None, FindPartnerInvoicesStatus] = UNSET,
    invoice_date: Union[Unset, None, str] = UNSET,
    invoice_date_range_start: Union[Unset, None, str] = UNSET,
    invoice_date_range_end: Union[Unset, None, str] = UNSET,
    due_date: Union[Unset, None, str] = UNSET,
    total: Union[Unset, None, float] = UNSET,
    balance: Union[Unset, None, float] = UNSET,
    carried_balance: Union[Unset, None, float] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, FindPartnerInvoicesResponse200]]:
    """Fetch a paginated list of invoices

     Fetch a paginated list of invoices. Default page is 0 and default size is 10. The maximum page size
    is 200

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindPartnerInvoicesSort]):
        status (Union[Unset, None, FindPartnerInvoicesStatus]):
        invoice_date (Union[Unset, None, str]):
        invoice_date_range_start (Union[Unset, None, str]):
        invoice_date_range_end (Union[Unset, None, str]):
        due_date (Union[Unset, None, str]):
        total (Union[Unset, None, float]):
        balance (Union[Unset, None, float]):
        carried_balance (Union[Unset, None, float]):
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindPartnerInvoicesResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        size=size,
        sort=sort,
        status=status,
        invoice_date=invoice_date,
        invoice_date_range_start=invoice_date_range_start,
        invoice_date_range_end=invoice_date_range_end,
        due_date=due_date,
        total=total,
        balance=balance,
        carried_balance=carried_balance,
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
    sort: Union[Unset, None, FindPartnerInvoicesSort] = UNSET,
    status: Union[Unset, None, FindPartnerInvoicesStatus] = UNSET,
    invoice_date: Union[Unset, None, str] = UNSET,
    invoice_date_range_start: Union[Unset, None, str] = UNSET,
    invoice_date_range_end: Union[Unset, None, str] = UNSET,
    due_date: Union[Unset, None, str] = UNSET,
    total: Union[Unset, None, float] = UNSET,
    balance: Union[Unset, None, float] = UNSET,
    carried_balance: Union[Unset, None, float] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, FindPartnerInvoicesResponse200]]:
    """Fetch a paginated list of invoices

     Fetch a paginated list of invoices. Default page is 0 and default size is 10. The maximum page size
    is 200

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindPartnerInvoicesSort]):
        status (Union[Unset, None, FindPartnerInvoicesStatus]):
        invoice_date (Union[Unset, None, str]):
        invoice_date_range_start (Union[Unset, None, str]):
        invoice_date_range_end (Union[Unset, None, str]):
        due_date (Union[Unset, None, str]):
        total (Union[Unset, None, float]):
        balance (Union[Unset, None, float]):
        carried_balance (Union[Unset, None, float]):
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindPartnerInvoicesResponse200]]
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
        sort=sort,
        status=status,
        invoice_date=invoice_date,
        invoice_date_range_start=invoice_date_range_start,
        invoice_date_range_end=invoice_date_range_end,
        due_date=due_date,
        total=total,
        balance=balance,
        carried_balance=carried_balance,
        company_id=company_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
    sort: Union[Unset, None, FindPartnerInvoicesSort] = UNSET,
    status: Union[Unset, None, FindPartnerInvoicesStatus] = UNSET,
    invoice_date: Union[Unset, None, str] = UNSET,
    invoice_date_range_start: Union[Unset, None, str] = UNSET,
    invoice_date_range_end: Union[Unset, None, str] = UNSET,
    due_date: Union[Unset, None, str] = UNSET,
    total: Union[Unset, None, float] = UNSET,
    balance: Union[Unset, None, float] = UNSET,
    carried_balance: Union[Unset, None, float] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, FindPartnerInvoicesResponse200]]:
    """Fetch a paginated list of invoices

     Fetch a paginated list of invoices. Default page is 0 and default size is 10. The maximum page size
    is 200

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindPartnerInvoicesSort]):
        status (Union[Unset, None, FindPartnerInvoicesStatus]):
        invoice_date (Union[Unset, None, str]):
        invoice_date_range_start (Union[Unset, None, str]):
        invoice_date_range_end (Union[Unset, None, str]):
        due_date (Union[Unset, None, str]):
        total (Union[Unset, None, float]):
        balance (Union[Unset, None, float]):
        carried_balance (Union[Unset, None, float]):
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindPartnerInvoicesResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        size=size,
        sort=sort,
        status=status,
        invoice_date=invoice_date,
        invoice_date_range_start=invoice_date_range_start,
        invoice_date_range_end=invoice_date_range_end,
        due_date=due_date,
        total=total,
        balance=balance,
        carried_balance=carried_balance,
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
    sort: Union[Unset, None, FindPartnerInvoicesSort] = UNSET,
    status: Union[Unset, None, FindPartnerInvoicesStatus] = UNSET,
    invoice_date: Union[Unset, None, str] = UNSET,
    invoice_date_range_start: Union[Unset, None, str] = UNSET,
    invoice_date_range_end: Union[Unset, None, str] = UNSET,
    due_date: Union[Unset, None, str] = UNSET,
    total: Union[Unset, None, float] = UNSET,
    balance: Union[Unset, None, float] = UNSET,
    carried_balance: Union[Unset, None, float] = UNSET,
    company_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, FindPartnerInvoicesResponse200]]:
    """Fetch a paginated list of invoices

     Fetch a paginated list of invoices. Default page is 0 and default size is 10. The maximum page size
    is 200

    Args:
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.
        sort (Union[Unset, None, FindPartnerInvoicesSort]):
        status (Union[Unset, None, FindPartnerInvoicesStatus]):
        invoice_date (Union[Unset, None, str]):
        invoice_date_range_start (Union[Unset, None, str]):
        invoice_date_range_end (Union[Unset, None, str]):
        due_date (Union[Unset, None, str]):
        total (Union[Unset, None, float]):
        balance (Union[Unset, None, float]):
        carried_balance (Union[Unset, None, float]):
        company_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Error, FindPartnerInvoicesResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
            sort=sort,
            status=status,
            invoice_date=invoice_date,
            invoice_date_range_start=invoice_date_range_start,
            invoice_date_range_end=invoice_date_range_end,
            due_date=due_date,
            total=total,
            balance=balance,
            carried_balance=carried_balance,
            company_id=company_id,
        )
    ).parsed
