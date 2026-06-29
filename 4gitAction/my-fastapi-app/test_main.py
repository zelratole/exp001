from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "os_info" in data

def test_read_item():
    response = client.get("/items/42?q=test-query")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "test-query"}