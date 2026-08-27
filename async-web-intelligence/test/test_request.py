import pytest
from src.http_client.requests_client import fetch_page
import requests
from unittest.mock import patch
@pytest.mark.parametrize("url",[
    "https://jobs.lever.co/entrata/661bbcc5-3514-4ba3-b616-8838da6c53ec",
    "https://job-boards.greenhouse.io/singlestore/jobs/7534083",
    "https://jobs.smartrecruiters.com/smartrecruiters/744000114676597-senior-software-engineer-python"
])
def test_succesful_request(url):
    response=fetch_page(url)
    assert response["status_code"]==200


def test_invalid_url():
    response = fetch_page("https://invalid-url-12345.com")

    assert "error" in response

def test_timeout():
    with patch("src.http_client.requests_client.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.Timeout

        response = fetch_page("https://example.com")

        assert response["error"] == "timeout error"
