Sure, let's create API endpoints for the mentioned ecommerce functionalities. We'll create three endpoints:

1. GET `/products` for product listing
2. GET `/products/{product_id}` for product details
3. POST `/cart` for adding product to cart

First, let's define our Pydantic models:

```python
from pydantic import BaseModel
from typing import Optional, List


class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


class ProductInCart(BaseModel):
    product_id: int
    quantity: int


class Cart(BaseModel):
    id: int
    products: List[ProductInCart]
```

Now, let's define a service layer. This is a simple example and doesn't include actual database operations. In a real-world application, you'd replace these with actual DB operations:

```python
from typing import Dict, Optional


class ProductService:
    """Service layer for handling product operations."""
    
    products: Dict[int, Product] = {}  # Example data, replace with DB operations in real application

    @classmethod
    def get_product_list(cls):
        return list(cls.products.values())

    @classmethod
    def get_product(cls, product_id: int) -> Optional[Product]:
        return cls.products.get(product_id)


class CartService:
    """Service layer for handling cart operations."""
    
    cart: Dict[int, Cart] = {}  # Example data, replace with DB operations in real application

    @classmethod
    def add_product(cls, cart_id: int, product_in_cart: ProductInCart) -> Cart:
        if cart_id not in cls.cart:
            cls.cart[cart_id] = Cart(id=cart_id, products=[product_in_cart])
        else:
            cls.cart[cart_id].products.append(product_in_cart)
        return cls.cart[cart_id]
```

Finally, let's create our FastAPI application and define the endpoints:

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/products", response_model=List[Product])
async def get_products():
    """
    Get the list of all products
    """
    return ProductService.get_product_list()

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """
    Get the details of a specific product
    """
    product = ProductService.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/cart", response_model=Cart)
async def add_product_to_cart(cart_id: int, product_in_cart: ProductInCart):
    """
    Add a product to the cart
    """
    return CartService.add_product(cart_id, product_in_cart)
```

This is a basic implementation and there are many enhancements you could add, such as authentication, more detailed validation, error handling, etc.