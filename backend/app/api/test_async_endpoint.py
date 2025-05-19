FastAPI has a built-in test client to help in testing API endpoints. We will use PyTest, a powerful Python testing framework, for our testing needs. Here is how to set up a testing environment for your FastAPI application.


Firstly, install pytest and pytest-asyncio using pip:

```bash
pip install pytest pytest-asyncio
```

Now, create a new file, `test_main.py`, in your project's root directory. In this file, we will write our tests.

```python
from fastapi.testclient import TestClient
import pytest
from main import app  # import your FastAPI instance

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI!"}
```

This is a simple test that checks the GET / request. It expects the status code to be 200 and the JSON response to be {"message": "Welcome to FastAPI!"}.

For integration tests that involve async functionality, pytest-asyncio comes in handy. Here's an example:

```python
@pytest.mark.asyncio
async def test_async_endpoint():
    response = await client.get("/async-endpoint")
    assert response.status_code == 200
    assert response.json() == {"message": "Async endpoint works!"}
```

Remember to replace "/async-endpoint" and {"message": "Async endpoint works!"} with your actual async endpoint and expected response.

To run the tests, simply run:

```bash
pytest
```

This structure allows you to write both unit tests and integration tests for your FastAPI application. Remember to write tests for all your API endpoints to ensure they work as expected.