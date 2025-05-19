Here's a simple example of a Login form component in React using hooks and prop-types. 

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './LoginForm.css';

/**
 * A login form component with input validation and error handling
 * @param {object} props - Component props
 * @param {Function} props.onSubmit - Callback function for form submission
 */
const LoginForm = ({ onSubmit }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (username === "" || password === "") {
      setError("Both fields are required");
      return;
    }

    onSubmit({ username, password });
  };

  return (
    <form className="login-form" onSubmit={handleSubmit}>
      <h2>Login</h2>
      {error && <div className="error">{error}</div>}
      <label htmlFor="username">Username:</label>
      <input
        type="text"
        id="username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <label htmlFor="password">Password:</label>
      <input
        type="password"
        id="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button type="submit">Login</button>
    </form>
  );
};

LoginForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
};

export default LoginForm;
```

For the CSS, you might have something like this:

```css
/* LoginForm.css */
.login-form {
  display: flex;
  flex-direction: column;
  width: 300px;
  margin: 0 auto;
}

.login-form label {
  margin-top: 1em;
}

.login-form input {
  margin-top: 0.5em;
}

.login-form button {
  margin-top: 1em;
}

.error {
  color: red;
}
```

This component includes input validation for empty fields and error handling. It also uses PropTypes to ensure the onSubmit prop is provided and that it is a function. The CSS is in a separate file and the styles are basic, but you can customize as needed.