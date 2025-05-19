Sure, here are the unit tests that you requested. We'll use `pytest` and `fastapi.testclient.TestClient` for testing.

```python
import pytest
from fastapi.testclient import TestClient
from main import app, ProductService, CartService, Product, ProductInCart

client = TestClient(app)

def test_get_products():
    ProductService.products = {1: Product(id=1, name="Test Product", price=100.0)}
    
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Test Product", "price": 100.0, "description": None}]

def test_get_product_success():
    ProductService.products = {1: Product(id=1, name="Test Product", price=100.0)}
    
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Product", "price": 100.0, "description": None}

def test_get_product_not_found():
    ProductService.products = {}
    
    response = client.get("/products/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}

def test_add_product_to_cart_success():
    CartService.cart = {}
    ProductService.products = {1: Product(id=1, name="Test Product", price=100.0)}
    
    response = client.post("/cart", json={"cart_id": 1, "product_in_cart": {"product_id": 1, "quantity": 1}})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "products": [{"product_id": 1, "quantity": 1}]}

def test_add_product_to_cart_validation_error():
    CartService.cart = {}
    ProductService.products = {1: Product(id=1, name="Test Product", price=100.0)}
    
    response = client.post("/cart", json={"cart_id": 1, "product_in_cart": {"product_id": "invalid", "quantity": 1}})
    assert response.status_code == 422  # Unprocessable Entity
```

These tests cover success cases, error cases, and data validation. Edge cases would depend on the specific business rules of your application. For example, you might want to test adding a product to the cart that is out of stock, adding a negative quantity of a product, adding a product that does not exist, etc.