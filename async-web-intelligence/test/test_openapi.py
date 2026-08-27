from pathlib import Path


def test_openapi_schema_exists():
    openapi_file = Path("openapi.yaml")

    assert openapi_file.exists()