# conftest.py

import pytest
from starlette.testclient import TestClient

from app.main import app

# Fixture function that provides a test client for the application
@pytest.fixture(scope="module")
def test_app():
    # Create a TestClient instance with the main FastAPI app
    client = TestClient(app)
    yield client  # The testing happens here