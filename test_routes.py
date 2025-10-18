"""Route tests using test doubles"""
from io import BytesIO

# smoke tests for routes
def test_home_renders(client):
  """
  tests if client renders home page

  Args:
      client (app): client app
  """
  resp = client.get("/")
  assert resp.status_code == 200
  # Basic smoke check: page contains upload form or title keywords
  assert b"Upload" in resp.data or b"Prediction" in resp.data or b"<form" in resp.data
  
def test_index_has_title(client):
  """
  tests if client renders home page with title
  """
  resp = client.get("/")
  assert resp.status_code == 200
  assert b"Hand Sign" in resp.data

def test_prediction_missing_file(client):
  """
  tests prediction route with missing file

  Args:
      client (app): client app
  """
  # No 'file' field
  resp = client.post("/prediction", data={}, content_type="multipart/form-data")
  assert resp.status_code == 200
  # App's error branch should render an error message
  assert b"File cannot be processed" in resp.data or b"error" in resp.data.lower()

def test_prediction_wrong_content_type(client):
  """
  tests prediction route with wrong content type

  Args:
      client (app): client app
  """
  # Send a request without multipart/form-data; Flask will still parse, but we ensure it doesn't 500
  resp = client.post("/prediction", data=b"raw", headers={"Content-Type": "application/octet-stream"})
  assert resp.status_code == 200  # app handles errors via template
  assert b"File cannot be processed" in resp.data or b"error" in resp.data.lower()
