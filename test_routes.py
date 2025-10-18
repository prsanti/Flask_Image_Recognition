"""Route tests using test doubles."""

# smoke tests for routes
def test_home_renders(client):
    """
    Test that the home page renders.

    Args:
        client (app): client app
    """
    resp = client.get("/")
    assert resp.status_code == 200
    # Basic smoke check: page contains upload form or title keywords
    assert (
        b"Upload" in resp.data
        or b"Prediction" in resp.data
        or b"<form" in resp.data
    )


def test_index_has_title(client):
    """
    Test that the home page contains the expected title text.
    """
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hand Sign" in resp.data


def test_prediction_missing_file(client):
    """
    Test prediction route with a missing file.

    Args:
        client (app): client app
    """
    # No 'file' field
    resp = client.post("/prediction", data={}, content_type="multipart/form-data")
    assert resp.status_code == 200
    # App's error branch should render an error message
    assert (
        b"File cannot be processed" in resp.data
        or b"error" in resp.data.lower()
    )


def test_prediction_wrong_content_type(client):
    """
    Test prediction route with a wrong content type.

    Args:
        client (app): client app
    """
    # Send request without multipart/form-data; ensure it does not 500
    resp = client.post(
        "/prediction",
        data=b"raw",
        headers={"Content-Type": "application/octet-stream"},
    )
    # App handles errors via template, should still be a 200 page response
    assert resp.status_code == 200
    assert (
        b"File cannot be processed" in resp.data
        or b"error" in resp.data.lower()
    )
