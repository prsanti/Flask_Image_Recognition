"""
Integration Tests for Sad Path Scenarios in Image Uploads
- This module contains integration tests for failure scenarios in image uploads to the Flask application.
"""

def test_missing_file(client):
    """Test the prediction route with a missing file."""
    response = client.post("/prediction", data={}, content_type="multipart/form-data")
    assert response.status_code == 200
    assert b"File cannot be processed." in response.data  # Check if the error message is displayed
