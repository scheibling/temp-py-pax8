from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.usage_summary import UsageSummary
from ...types import Response


def _get_kwargs(
    usage_summary_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/usage-summaries/{usageSummaryId}".format(client.base_url, usageSummaryId=usage_summary_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[UsageSummary]:
    if response.status_code == 200:
        response_200 = UsageSummary.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[UsageSummary]:
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
) -> Response[UsageSummary]:
    """Fetch a usage summary by usageSummaryId

     Fetch a paginated list of usage summaries. Default page is 0 and default size is 10. The maximum
    page size is 200

    Args:
        usage_summary_id (str):

    Returns:
        Response[UsageSummary]
    """

    kwargs = _get_kwargs(
        usage_summary_id=usage_summary_id,
        client=client,
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
) -> Optional[UsageSummary]:
    """Fetch a usage summary by usageSummaryId

     Fetch a paginated list of usage summaries. Default page is 0 and default size is 10. The maximum
    page size is 200

    Args:
        usage_summary_id (str):

    Returns:
        Response[UsageSummary]
    """

    return sync_detailed(
        usage_summary_id=usage_summary_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    usage_summary_id: str,
    *,
    client: Client,
) -> Response[UsageSummary]:
    """Fetch a usage summary by usageSummaryId

     Fetch a paginated list of usage summaries. Default page is 0 and default size is 10. The maximum
    page size is 200

    Args:
        usage_summary_id (str):

    Returns:
        Response[UsageSummary]
    """

    kwargs = _get_kwargs(
        usage_summary_id=usage_summary_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    usage_summary_id: str,
    *,
    client: Client,
) -> Optional[UsageSummary]:
    """Fetch a usage summary by usageSummaryId

     Fetch a paginated list of usage summaries. Default page is 0 and default size is 10. The maximum
    page size is 200

    Args:
        usage_summary_id (str):

    Returns:
        Response[UsageSummary]
    """

    return (
        await asyncio_detailed(
            usage_summary_id=usage_summary_id,
            client=client,
        )
    ).parsed
