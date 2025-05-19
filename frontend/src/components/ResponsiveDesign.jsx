Here is a simple example of a responsive design component in React:

```jsx
// Necessary Imports
import React from 'react';
import PropTypes from 'prop-types';
import './ResponsiveDesign.css';

/**
 * ResponsiveDesign component
 * @param {string} view - The current view (mobile, tablet, desktop)
 * @param {any} children - The children components
 * @returns {JSX.Element}
 *
 * Usage:
 * <ResponsiveDesign view="mobile">
 *   <MyComponent />
 * </ResponsiveDesign>
 */
const ResponsiveDesign = ({ view, children }) => {
  return (
    <div className={`responsive-design ${view}`}>
      {children}
    </div>
  );
};

// PropTypes 
ResponsiveDesign.propTypes = {
  view: PropTypes.oneOf(['mobile', 'tablet', 'desktop']).isRequired,
  children: PropTypes.node.isRequired,
};

// Export statement
export default ResponsiveDesign;
```

Now, you need to define the CSS for different views:

```css
/* ResponsiveDesign.css */

.responsive-design.mobile {
  width: 100%;
  padding: 16px;
}

.responsive-design.tablet {
  max-width: 768px;
  padding: 24px;
  margin: 0 auto;
}

.responsive-design.desktop {
  max-width: 1200px;
  padding: 32px;
  margin: 0 auto;
}
```

This very basic example will render its children within a container that has different max-width and padding based on the prop `view`. This is a very simplified example and a real world application would probably use a more sophisticated approach, like CSS media queries or a CSS-in-JS solution with theme support, for responsive design.