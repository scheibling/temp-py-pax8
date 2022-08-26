from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.invoice import Invoice
from ...types import Response


def _get_kwargs(
    invoice_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/invoices/{invoiceId}".format(client.base_url, invoiceId=invoice_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Invoice]:
    if response.status_code == 200:
        response_200 = Invoice.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Invoice]:
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
) -> Response[Invoice]:
    """Fetch an invoice by invoiceId

     Fetch a paginated list of invoices. Default page is 0 and default size is 10. The maximum page size
    is 200

    Args:
        invoice_id (str):

    Returns:
        Response[Invoice]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
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
) -> Optional[Invoice]:
    """Fetch an invoice by invoiceId

     Fetch a paginated list of invoices. Default page is 0 and default size is 10. The maximum page size
    is 200

    Args:
        invoice_id (str):

    Returns:
        Response[Invoice]
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: Client,
) -> Response[Invoice]:
    """Fetch an invoice by invoiceId

     Fetch a paginated list of invoices. Default page is 0 and default size is 10. The maximum page size
    is 200

    Args:
        invoice_id (str):

    Returns:
        Response[Invoice]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    invoice_id: str,
    *,
    client: Client,
) -> Optional[Invoice]:
    """Fetch an invoice by invoiceId

     Fetch a paginated list of invoices. Default page is 0 and default size is 10. The maximum page size
    is 200

    Args:
        invoice_id (str):

    Returns:
        Response[Invoice]
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
        )
    ).parsed
