Here are the comprehensive unit tests for the "DeploymentPipeline" component:

```jsx
// Necessary imports
import React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import DeploymentPipeline from './DeploymentPipeline';

// Mock props
const mockProps = {
  task: 'Test Task',
  requirements: [
    { id: 1, name: 'Requirement 1' },
    { id: 2, name: 'Requirement 2' },
  ],
};

describe('DeploymentPipeline', () => {
  test('renders without crashing', () => {
    render(<DeploymentPipeline {...mockProps} />);
    const taskContainer = screen.getByTestId('task-container');
    expect(taskContainer).toBeInTheDocument();
  });

  test('renders task title correctly', () => {
    render(<DeploymentPipeline {...mockProps} />);
    const taskTitle = screen.getByText(mockProps.task);
    expect(taskTitle).toBeInTheDocument();
  });

  test('renders requirements correctly', () => {
    render(<DeploymentPipeline {...mockProps} />);
    mockProps.requirements.forEach((requirement) => {
      const listItem = screen.getByText(requirement.name);
      expect(listItem).toBeInTheDocument();
    });
  });

  test('shows error when task or requirements are missing', () => {
    render(<DeploymentPipeline />);
    const errorDiv = screen.getByText('Error: Task and requirements are required!');
    expect(errorDiv).toBeInTheDocument();
  });
});
```

In this test suite, we're testing if the component renders without crashing, if the task title and requirements are rendered correctly, and if an error shows up when task or requirements props are missing.

Before running these tests, make sure to install Jest and React Testing Library:

```
npm install --save-dev jest @testing-library/react
```

Then, you can run these tests with the `npm test` command.

Please note that the actual DeploymentPipeline component should be updated to include 'data-testid' attributes for elements that have to be located in tests:

```jsx
<TaskContainer data-testid="task-container">
  <TaskTitle>{task}</TaskTitle>
  <RequirementsList>
    {requirements.map((requirement) => (
      <RequirementItem key={requirement.id}>
        {requirement.name}
      </RequirementItem>
    ))}
  </RequirementsList>
</TaskContainer>
```

And when no task or requirements are provided:

```jsx
if (!task || !requirements) {
  return <div data-testid="error-div">Error: Task and requirements are required!</div>;
}
```

This is to ensure the elements can be easily located and tested.