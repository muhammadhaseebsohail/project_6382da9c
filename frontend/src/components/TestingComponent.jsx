For this task, we will create a TestingComponent that takes a testing setup object as a prop and displays the task and its requirements. 

Here's the complete React component:

```jsx
import React from 'react';
import PropTypes from 'prop-types';
import './TestingComponent.css';

/**
 * TestingComponent - A component that displays a testing task and its requirements.
 * 
 * @param {object} props - The props for the component.
 * @param {object} props.testingSetup - The testing setup for the task.
 * @param {string} props.testingSetup.task - The task name.
 * @param {string[]} props.testingSetup.requirements - The requirements for the task.
 */
const TestingComponent = ({ testingSetup }) => {
  const { task, requirements } = testingSetup;

  // Error handling if no testing setup is provided
  if (!testingSetup) {
    return <p>Error: No testing setup provided.</p>;
  }

  return (
    <div className="testing-component">
      <h2>{task}</h2>
      <ul>
        {requirements.map((requirement, index) => (
          <li key={index}>{requirement}</li>
        ))}
      </ul>
    </div>
  );
};

TestingComponent.propTypes = {
  testingSetup: PropTypes.shape({
    task: PropTypes.string.isRequired,
    requirements: PropTypes.arrayOf(PropTypes.string).isRequired,
  }).isRequired,
};

export default TestingComponent;
```

CSS styling:

```css
/* TestingComponent.css */

.testing-component {
  border: 1px solid #ccc;
  padding: 20px;
  margin-bottom: 20px;
}

.testing-component h2 {
  margin: 0 0 10px 0;
}

.testing-component ul {
  list-style-type: none;
  padding: 0;
}

.testing-component ul li {
  margin-bottom: 5px;
}
```

The PropTypes for the component are defined as follows:

```jsx
TestingComponent.propTypes = {
  testingSetup: PropTypes.shape({
    task: PropTypes.string.isRequired,
    requirements: PropTypes.arrayOf(PropTypes.string).isRequired,
  }).isRequired,
};
```

Finally, we export the TestingComponent using the `export default` statement.

```jsx
export default TestingComponent;
```