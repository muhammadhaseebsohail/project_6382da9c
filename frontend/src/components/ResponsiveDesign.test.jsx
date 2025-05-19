Here are the unit tests for the ResponsiveDesign component:

```jsx
// Necessary Imports
import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import ResponsiveDesign from './ResponsiveDesign';

describe('ResponsiveDesign', () => {
  // Test for component rendering
  test('renders ResponsiveDesign component', () => {
    render(<ResponsiveDesign view="mobile"><div>Test</div></ResponsiveDesign>);
    expect(screen.getByText('Test')).toBeInTheDocument();
  });

  // Test for prop validation
  test('renders with correct view class', () => {
    const { container } = render(<ResponsiveDesign view="desktop"><div>Test</div></ResponsiveDesign>);
    expect(container.firstChild).toHaveClass('desktop');
  });

  // Edge case: Invalid prop type for view
  test('throws error with invalid view prop', () => {
    console.error = jest.fn(); // to prevent console.error output in test run
    expect(() => render(<ResponsiveDesign view="notAView"><div>Test</div></ResponsiveDesign>)).toThrowError();
    expect(console.error).toHaveBeenCalled();
  });
});
```

In this test suite, we have three tests:

1. The first test verifies that the component renders correctly.
2. The second test verifies that the `view` prop correctly sets the class name on the top-level `div`.
3. The last test checks an edge case where an invalid value for the `view` prop is passed. This test should fail because PropTypes validation will fail and an error will be thrown. We mock `console.error` to prevent the error from being logged to the console during the test run.

Please note that PropTypes only checks for prop type errors in development mode and not in production. Therefore, the last test will only fail in development mode. If you want to enforce prop types in production as well, consider using TypeScript instead.