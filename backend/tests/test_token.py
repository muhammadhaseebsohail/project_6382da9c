Here are the unit tests for the FastAPI endpoints:

```python
from fastapi.testclient import TestClient
from main import app, get_password_hash
from pydantic import EmailStr

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/",
        json={"email": "test@test.com", "password": "testpassword", "is_active": True},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "test@test.com"
    assert "id" in data
    assert "password" not in data

def test_create_user_invalid_input():
    # Test creating user with invalid email
    response = client.post(
        "/users/",
        json={"email": "notanemail", "password": "testpassword", "is_active": True},
    )
    assert response.status_code == 422
    assert response.json() == {'detail': [{'loc': ['body', 'email'], 'msg': 'value is not a valid email address', 'type': 'value_error.email'}]}

def test_create_user_existing_email():
    # Test creating user with an already used email
    response = client.post(
        "/users/",
        json={"email": "test@test.com", "password": "testpassword", "is_active": True},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}

def test_token():
    # User login
    response = client.post(
        "/token",
        data={"username": "test@test.com", "password": "testpassword"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_token_invalid_input():
    # Test login with incorrect password
    response = client.post(
        "/token",
        data={"username": "test@test.com", "password": "wrongpassword"},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect email or password"}

def test_token_non_existing_user():
    # Test login with non existing user
    response = client.post(
        "/token",
        data={"username": "nonexisting@test.com", "password": "testpassword"},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect email or password"}
```

In these tests, we use the `TestClient` from `fastapi.testclient` to make requests to our app. Each function represents one test case. We use assertions to verify that the response from the server is what we expect.

- `test_create_user` tests the "/users/" POST request with valid data.
- `test_create_user_invalid_input` tests the "/users/" POST request with invalid data.
- `test_create_user_existing_email` tests the "/users/" POST request with an existing email.
- `test_token` tests the "/token" POST request with valid data.
- `test_token_invalid_input` tests the "/token" POST request with invalid data.
- `test_token_non_existing_user` tests the "/token" POST request with a non-existing user.

For the sake of simplicity, we are using a dummy database. In a real application, you would need to reset the database before each test to ensure a clean state. You would also need to handle the case where a user with the same email already exists in the database.