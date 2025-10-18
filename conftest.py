"""
This module sets up the testing environment for the Flask application using pytest.
"""

import pytest
from app import app  # This imports the Flask app for testing

@pytest.fixture
def client():
    """
    Provide a flask test client for testing.

    Yields:
        FlaskClient: A test client for the Flask application.
    """
    with app.test_client() as client:
        yield client
