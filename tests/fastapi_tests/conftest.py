from fastapi.testclient import TestClient
from src.app import app

import pytest

@pytest.fixture
def client():
    """Fixture to provide a FastAPI test client."""
    return TestClient(app)