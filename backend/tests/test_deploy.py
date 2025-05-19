Here's how you can write tests for the provided FastAPI endpoint using pytest and FastAPI's TestClient. This includes tests for success cases, error cases, data validation, and edge cases.

```python
from fastapi.testclient import TestClient
from main import app, DeploymentModel
from jose import jwt
import pytest

client = TestClient(app)

def test_deploy_success():
    """
    Test successful pipeline deployment
    """
    # generate a valid token for testing
    token = jwt.encode({"sub": "testuser"}, "secret", algorithm="HS256")
    response = client.post("/deploy", json={"ci": True, "cd": True}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"ci": True, "cd": True}

def test_deploy_error():
    """
    Test pipeline deployment with invalid token
    """
    response = client.post("/deploy", json={"ci": True, "cd": True}, headers={"Authorization": "Bearer invalid_token"})
    assert response.status_code == 403

def test_data_validation():
    """
    Test data validation for pipeline deployment
    """
    token = jwt.encode({"sub": "testuser"}, "secret", algorithm="HS256")
    response = client.post("/deploy", json={"ci": "invalid", "cd": "invalid"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 422

def test_edge_cases():
    """
    Test edge case with missing data for pipeline deployment
    """
    token = jwt.encode({"sub": "testuser"}, "secret", algorithm="HS256")
    response = client.post("/deploy", json={}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"ci": False, "cd": False}
```
In these tests:

- `test_deploy_success` tests a successful pipeline deployment with valid data and token.
- `test_deploy_error` tests the endpoint with an invalid token. It should return a 403 status code.
- `test_data_validation` tests the data validation by sending invalid data for ci and cd fields. It should return a 422 status code.
- `test_edge_cases` tests the endpoint with missing data for ci and cd fields. According to the Pydantic model, these fields are optional and default to False, so the endpoint should return a 200 status code and a response with ci and cd set to False.

These tests can be run using `pytest` from the command line.