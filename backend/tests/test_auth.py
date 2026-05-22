import time
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
TEST_EMAIL = f"test_{int(time.time())}@example.com"
TEST_PASSWORD = "securepass123"

def test_register_success():
    response = client.post("/auth/register", json={"email": TEST_EMAIL, "password": TEST_PASSWORD})
    assert response.status_code == 200
    assert "id" in response.json()

def test_login_success():
    response = client.post("/auth/login", json={"email": TEST_EMAIL, "password": TEST_PASSWORD})
    assert response.status_code == 200
    assert "access_token" in response.json()