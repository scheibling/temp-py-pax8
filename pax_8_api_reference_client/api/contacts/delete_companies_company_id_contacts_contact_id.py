from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    company_id: str,
    contact_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/companies/{companyId}/contacts/{contactId}".format(
        client.base_url, companyId=company_id, contactId=contact_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    company_id: str,
    contact_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Error]]:
    """Delete a contact

     Deletes a contact

    Args:
        company_id (str):
        contact_id (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        contact_id=contact_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    company_id: str,
    contact_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Error]]:
    """Delete a contact

     Deletes a contact

    Args:
        company_id (str):
        contact_id (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        company_id=company_id,
        contact_id=contact_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    contact_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Error]]:
    """Delete a contact

     Deletes a contact

    Args:
        company_id (str):
        contact_id (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        contact_id=contact_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    company_id: str,
    contact_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Error]]:
    """Delete a contact

     Deletes a contact

    Args:
        company_id (str):
        contact_id (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            contact_id=contact_id,
            client=client,
        )
    ).parsed
