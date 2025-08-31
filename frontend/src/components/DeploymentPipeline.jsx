Here is a simple React component called "DeploymentPipeline" that represents a task with its requirements. This component can be reused in any part of the application that needs to display a task. The component uses TypeScript interfaces for props validation, and CSS-in-JS with the styled-components library for styling.

```jsx
// Necessary imports
import React from 'react';
import styled from 'styled-components';

// TypeScript interfaces for props validation
interface Requirement {
  id: number;
  name: string;
}

interface DeploymentPipelineProps {
  task: string;
  requirements: Requirement[];
}

// Styled-components for CSS-in-JS
const TaskContainer = styled.div`
  display: flex;
  flex-direction: column;
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 5px;
  margin-bottom: 20px;
`;

const TaskTitle = styled.h2`
  margin: 0;
  margin-bottom: 10px;
`;

const RequirementsList = styled.ul`
  margin: 0;
  padding: 0;
  list-style-type: none;
`;

const RequirementItem = styled.li`
  margin-bottom: 5px;
`;

// React functional component
const DeploymentPipeline: React.FC<DeploymentPipelineProps> = ({ task, requirements }) => {
  // Error handling for missing props
  if (!task || !requirements) {
    return <div>Error: Task and requirements are required!</div>;
  }

  // Loading state
  if (!task || !requirements) {
    return <div>Loading...</div>;
  }

  return (
    <TaskContainer>
      <TaskTitle>{task}</TaskTitle>
      <RequirementsList>
        {requirements.map((requirement) => (
          <RequirementItem key={requirement.id}>
            {requirement.name}
          </RequirementItem>
        ))}
      </RequirementsList>
    </TaskContainer>
  );
};

// Export the component
export default DeploymentPipeline;
```

With this component, you can display any task with its requirements. The component is reusable, maintainable, and follows best practices of React and TypeScript.