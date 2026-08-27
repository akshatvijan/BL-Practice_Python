import pytest
import time
import asyncio
from src.http_client.async_gather import async_fetch_many
from unittest.mock import patch

@pytest.mark.anyio
async def test_concurrent_execution():
    urls = [
        "https://jobs.lever.co/entrata/661bbcc5-3514-4ba3-b616-8838da6c53ec",
        "https://job-boards.greenhouse.io/singlestore/jobs/7534083",
        "https://jobs.smartrecruiters.com/smartrecruiters/744000114676597-senior-software-engineer-python"
    ]
    start=asyncio.get_event_loop().time()
    result=await async_fetch_many(urls)
    end=asyncio.get_event_loop().time()

    assert start-end<30
    assert len(result)==3


@pytest.mark.anyio
async def test_partial_failure():
    urls=[
        "url1",
        "url2",
        "url3"
    ]
    responses= [
        {
            "url": "url1",
            "status_code": 200,
            "content": "success"
        },
        {
            "url": "url2",
            "error": "timeout error"
        },
        {
            "url": "url3",
            "status_code": 200,
            "content": "success"
        }
    ]
    async def response_fetch(url):
        for r in responses:
            if r["url"]==url:
                return r
             
    with patch("src.http_client.async_gather.async_fetch",side_effect=response_fetch): 
        result = await async_fetch_many(urls)
        

    

    assert len(result) == 3
    assert result[0]["status_code"] == 200
    assert "error" in result[1]
    assert result[2]["status_code"] == 200

   

    

    