from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange
    expected_status = 200

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == expected_status
    assert isinstance(response.json(), dict)