Here's an example of how you could structure these components:

```jsx
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './HomePage.css';

// Product component
const Product = ({ product, onAddToCart }) => {

  return (
    <div className="product">
      <img src={product.image} alt={product.name} />
      <h2>{product.name}</h2>
      <p>{product.description}</p>
      <button onClick={() => onAddToCart(product)}>Add to cart</button>
    </div>
  );
}

Product.propTypes = {
  product: PropTypes.shape({
    image: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
  }).isRequired,
  onAddToCart: PropTypes.func.isRequired,
};

// HomePage component
const HomePage = () => {
  const [products, setProducts] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/products') // Replace with your API endpoint
      .then((res) => {
        if (!res.ok) { throw res; }
        return res.json();
      })
      .then((data) => {
        setProducts(data);
        setIsLoading(false);
      })
      .catch((err) => {
        setError(err);
        setIsLoading(false);
      });
  }, []);

  const handleAddToCart = (product) => {
    // Implement add to cart functionality here
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error loading products...</div>;
  }

  return (
    <div className="home">
      {products.map((product) => (
        <Product key={product.id} product={product} onAddToCart={handleAddToCart} />
      ))}
    </div>
  );
};

export { HomePage, Product };
```

CSS styling (HomePage.css):

```css
.home {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.product {
  flex: 1 0 21%; /* four items per row */
  margin: 1%;
  padding: 1em;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.product img {
  width: 100%;
  height: auto;
}
```

In this example, the `HomePage` component fetches a list of products from a server (replace '/api/products' with your actual API endpoint), displays a loading message while the data is being fetched, and handles any errors that might occur during the fetch. The products are then passed to the `Product` component for display. 

The `Product` component displays the product image, name, and description, and provides an "Add to cart" button. When this button is clicked, the `onAddToCart` function is called with the product as an argument. This function can then be used to update the shopping cart. Both the `HomePage` and `Product` components are exported for use elsewhere in the application.