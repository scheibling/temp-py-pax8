from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.find_partner_invoice_items_response_200 import FindPartnerInvoiceItemsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    invoice_id: str,
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
) -> Dict[str, Any]:
    url = "{}/invoices/{invoiceId}/items".format(client.base_url, invoiceId=invoice_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, FindPartnerInvoiceItemsResponse200]]:
    if response.status_code == 200:
        response_200 = FindPartnerInvoiceItemsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, FindPartnerInvoiceItemsResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    invoice_id: str,
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
) -> Response[Union[Error, FindPartnerInvoiceItemsResponse200]]:
    """Fetch a paginated list of items for an invoice

     Fetch a paginated list of invoice items. Default page is 0 and default size is 10. The maximum page
    size is 200

    Args:
        invoice_id (str):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.

    Returns:
        Response[Union[Error, FindPartnerInvoiceItemsResponse200]]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
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
    invoice_id: str,
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
) -> Optional[Union[Error, FindPartnerInvoiceItemsResponse200]]:
    """Fetch a paginated list of items for an invoice

     Fetch a paginated list of invoice items. Default page is 0 and default size is 10. The maximum page
    size is 200

    Args:
        invoice_id (str):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.

    Returns:
        Response[Union[Error, FindPartnerInvoiceItemsResponse200]]
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
        page=page,
        size=size,
    ).parsed


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
) -> Response[Union[Error, FindPartnerInvoiceItemsResponse200]]:
    """Fetch a paginated list of items for an invoice

     Fetch a paginated list of invoice items. Default page is 0 and default size is 10. The maximum page
    size is 200

    Args:
        invoice_id (str):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.

    Returns:
        Response[Union[Error, FindPartnerInvoiceItemsResponse200]]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
        page=page,
        size=size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    invoice_id: str,
    *,
    client: Client,
    page: Union[Unset, None, float] = 0.0,
    size: Union[Unset, None, float] = 10.0,
) -> Optional[Union[Error, FindPartnerInvoiceItemsResponse200]]:
    """Fetch a paginated list of items for an invoice

     Fetch a paginated list of invoice items. Default page is 0 and default size is 10. The maximum page
    size is 200

    Args:
        invoice_id (str):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):  Default: 10.0.

    Returns:
        Response[Union[Error, FindPartnerInvoiceItemsResponse200]]
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            page=page,
            size=size,
        )
    ).parsed
