from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.contact import Contact
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    company_id: str,
    *,
    client: Client,
    json_body: Contact,
) -> Dict[str, Any]:
    url = "{}/companies/{companyId}/contacts".format(client.base_url, companyId=company_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Contact, Error]]:
    if response.status_code == 200:
        response_200 = Contact.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Contact, Error]]:
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
    json_body: Contact,
) -> Response[Union[Contact, Error]]:
    """Create a new Contact

     Creates a new Contact

    Args:
        company_id (str):
        json_body (Contact):

    Returns:
        Response[Union[Contact, Error]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        json_body=json_body,
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
    json_body: Contact,
) -> Optional[Union[Contact, Error]]:
    """Create a new Contact

     Creates a new Contact

    Args:
        company_id (str):
        json_body (Contact):

    Returns:
        Response[Union[Contact, Error]]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: Client,
    json_body: Contact,
) -> Response[Union[Contact, Error]]:
    """Create a new Contact

     Creates a new Contact

    Args:
        company_id (str):
        json_body (Contact):

    Returns:
        Response[Union[Contact, Error]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    company_id: str,
    *,
    client: Client,
    json_body: Contact,
) -> Optional[Union[Contact, Error]]:
    """Create a new Contact

     Creates a new Contact

    Args:
        company_id (str):
        json_body (Contact):

    Returns:
        Response[Union[Contact, Error]]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
