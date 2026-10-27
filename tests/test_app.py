
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_returns_success(client):
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()
    assert data["message"] == "Flask CI/CD Pipeline is running!"
    assert data["status"] == "success"
    assert data["version"] == "1.0.0"


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
