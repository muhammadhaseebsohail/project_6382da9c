Here's how you can test the LoginForm component using Jest and React Testing Library:

```jsx
// LoginForm.test.js
import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import LoginForm from './LoginForm';

describe('<LoginForm />', () => {
  let component;
  const mockSubmit = jest.fn();

  beforeEach(() => {
    component = render(<LoginForm onSubmit={mockSubmit} />);
  });

  test('renders form', () => {
    expect(component.container.querySelector('.login-form')).toBeDefined();
  });

  test('renders username and password inputs', () => {
    expect(component.container.querySelector('#username')).toBeDefined();
    expect(component.container.querySelector('#password')).toBeDefined();
  });

  test('renders login button', () => {
    expect(component.getByText('Login')).toBeDefined();
  });

  test('inputs are empty on mount', () => {
    expect(component.container.querySelector('#username').value).toBe('');
    expect(component.container.querySelector('#password').value).toBe('');
  });

  test('submits form with username and password', () => {
    const username = component.container.querySelector('#username');
    const password = component.container.querySelector('#password');
    const form = component.container.querySelector('.login-form');

    fireEvent.change(username, { target: { value: 'testuser' } });
    fireEvent.change(password, { target: { value: 'testpass' } });
    fireEvent.submit(form);

    expect(mockSubmit).toHaveBeenCalled();
    expect(mockSubmit).toHaveBeenCalledWith({
      username: 'testuser',
      password: 'testpass',
    });
  });

  test('does not submit form if username or password is empty', () => {
    const username = component.container.querySelector('#username');
    const form = component.container.querySelector('.login-form');

    fireEvent.change(username, { target: { value: 'testuser' } });
    fireEvent.submit(form);

    expect(mockSubmit).not.toHaveBeenCalled();
  });

  test('shows error message if form validation fails', () => {
    const form = component.container.querySelector('.login-form');

    fireEvent.submit(form);
    expect(component.getByText('Both fields are required')).toBeDefined();
  });
});
```

In these tests, we first render the component with a mock onSubmit function. Then we check if the form, inputs, and button are rendered correctly, and if the inputs are empty to start with. We also simulate user interactions by changing input values and submitting the form, and check if the onSubmit function is called with the correct arguments. We also test edge cases where the form should not be submitted and an error message should be displayed.