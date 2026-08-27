import pytest
import httpx
from src.http_client.async_gather import async_fetch
from src.http_client.async_gather import async_fetch_many
from unittest.mock import patch
@pytest.mark.anyio
async def test_async_request():
    response=await async_fetch("https://jobs.lever.co/entrata/661bbcc5-3514-4ba3-b616-8838da6c53ec")
    assert response["status_code"]==200

@pytest.fixture
def url():
    return [
    "https://jobs.lever.co/entrata/661bbcc5-3514-4ba3-b616-8838da6c53ec",
    "https://job-boards.greenhouse.io/singlestore/jobs/7534083",
    "https://jobs.smartrecruiters.com/smartrecruiters/744000114676597-senior-software-engineer-python"
]

@pytest.mark.anyio
async def test_many_asyn_request(url):
    result= await async_fetch_many(url)
    for r in result:
        assert r["status_code"]==200

    

@pytest.mark.anyio
@pytest.mark.parametrize("status_code,error", [
    (400, "Client error"),
    (500, "Server error")
])
async def test_http_error(status_code, error):
    with patch("src.http_client.async_gather.httpx.AsyncClient.get") as get:
        response = httpx.Response(
            status_code=status_code,
            request=httpx.Request("GET", "https://example.com")
        )

        get.return_value = response

        r = await async_fetch("https://example.com")

        assert r["status_code"] == status_code
        assert r["error"] == error
