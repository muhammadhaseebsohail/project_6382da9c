Sure, here's how you could structure the tests for these components:

```jsx
// Import necessary libraries
import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { HomePage, Product } from './HomePage';

// Mock Product
const mockProduct = {
  image: 'https://example.com/image.jpg',
  name: 'Test Product',
  description: 'This is a test product',
};

// Test for the Product component
describe('Product', () => {
  it('renders without crashing', () => {
    const { getByText } = render(<Product product={mockProduct} onAddToCart={() => {}} />);
    expect(getByText('Test Product')).toBeInTheDocument();
  });

  it('calls onAddToCart when the button is clicked', () => {
    const onAddToCart = jest.fn();
    const { getByText } = render(<Product product={mockProduct} onAddToCart={onAddToCart} />);
    fireEvent.click(getByText('Add to cart'));
    expect(onAddToCart).toHaveBeenCalled();
  });
});

// Mock fetch
global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true,
    json: () => Promise.resolve([mockProduct]),
  })
);

// Test for the HomePage component
describe('HomePage', () => {
  beforeEach(() => {
    fetch.mockClear();
  });

  it('renders without crashing', async () => {
    render(<HomePage />);
    await waitFor(() => expect(fetch).toHaveBeenCalledTimes(1));
  });

  it('displays products after fetching data', async () => {
    render(<HomePage />);
    await waitFor(() => expect(fetch).toHaveBeenCalledTimes(1));
    expect(screen.getByText('Test Product')).toBeInTheDocument();
  });

  it('displays error message when fetching fails', async () => {
    fetch.mockImplementationOnce(() => Promise.reject('API is down'));
    const { getByText } = render(<HomePage />);
    await waitFor(() => expect(fetch).toHaveBeenCalledTimes(1));
    expect(getByText('Error loading products...')).toBeInTheDocument();
  });
});
```

In this test, we first test the `Product` component by checking if it renders without crashing and if it calls the `onAddToCart` function when the "Add to cart" button is clicked.

Then we test the `HomePage` component. We use `jest.fn()` to create a mock function that simulates fetching data from an API. We check if the component renders without crashing, if it displays the products after fetching the data, and if it displays an error message when the fetch fails.

The `waitFor` function from React Testing Library is used to wait for the fetch to complete before making assertions. This is important because the fetch is asynchronous and we need to make sure that it has completed before we can accurately test the results. 

Also, we use `beforeEach` to clear the mock fetch before each test to ensure that each test starts with a clean slate.