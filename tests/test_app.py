import pytest
from httpx import ASGITransport, AsyncClient
from application.main import app


@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
