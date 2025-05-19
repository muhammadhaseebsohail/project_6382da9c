You can use the `TestClient` from `fastapi.testclient` to write tests for your endpoints. Here's how you could do it:

```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .main import app, get_db
from . import models, schemas, services

# Setup test database and override dependencies
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_product():
    response = client.post(
        "/products/",
        json={"name": "product1", "description": "product description", "price": 50.5},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "product1"
    assert data["description"] == "product description"
    assert data["price"] == 50.5
    assert "id" in data


def test_read_product():
    # create a new product
    product = services.create_product(
        db=TestingSessionLocal(),
        product=schemas.ProductCreate(
            name="product1", description="product description", price=50.5
        ),
    )
    response = client.get(f"/products/{product.id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "product1"
    assert data["description"] == "product description"
    assert data["price"] == 50.5
    assert data["id"] == product.id

    # try to get a non existing product
    response = client.get("/products/999")
    assert response.status_code == 404, response.text
    assert response.json() == {"detail": "Product not found"}


def test_create_user():
    response = client.post(
        "/users/",
        json={"email": "user1@test.com", "is_active": True, "password": "password"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "user1@test.com"
    assert data["is_active"] == True
    assert "id" in data
    assert "products" in data


def test_read_user():
    # create a new user
    user = services.create_user(
        db=TestingSessionLocal(),
        user=schemas.UserCreate(email="user1@test.com", password="password"),
    )
    response = client.get(f"/users/{user.id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "user1@test.com"
    assert data["is_active"] == True
    assert data["id"] == user.id
    assert data["products"] == []

    # try to get a non existing user
    response = client.get("/users/999")
    assert response.status_code == 404, response.text
    assert response.json() == {"detail": "User not found"}
```

This script creates a separate database for testing and overrides the `get_db` dependency to use this database. It then tests each of the four endpoints for both success and error cases. For the `read_*` endpoints, it tests the case where the requested item does not exist. For the `create_*` endpoints, it tests the case where the data is valid. You can expand these tests to cover more edge cases and invalid data cases as needed.