"""
Acceptance Tests for Happy Path Scenarios in Image Uploads
- This module contains acceptance tests for successful image uploads to the Flask application.
"""

from io import BytesIO

def test_acceptance_successful_upload(client):
    """
    Test Case: Successful Upload of a Valid Image File
    - Purpose: Ensure the application accepts a valid image file upload and provides a prediction.
    - Method:
        - Create a mock valid image file with minimal valid data.
        - Simulate a POST request to the `/prediction` route with the file.
        - Assert the response status code is 200.
        - Verify that the response data includes the keyword 'Prediction.'
    """
    img_data = BytesIO(b"fake_image_data")  # Simulated valid image data
    img_data.name = "test_image.jpg"

    response = client.post(
        "/prediction",
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"Prediction" in response.data


def test_acceptance_valid_large_image(client):
    """
    Test Case: Upload of a Valid Large Image File
    - Purpose: Check if the system accepts large but valid image files without errors
    - Method:
        - Create a mock large image file by repeating mock image data multiple times.
        - Simulate a POST request to the `/prediction` route with the file.
        - Assert the response status code is 200.
        - Verify the presence of 'Prediction' in the response data.
    """
    img_data = BytesIO(b"fake_large_image_data" * 1000)  # Simulating a large image
    img_data.name = "large_image.jpg"

    response = client.post(
        "/prediction",
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"Prediction" in response.data
