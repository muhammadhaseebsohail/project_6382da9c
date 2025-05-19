This task seems to be more related to DevOps and CI/CD pipelines which involve tools such as Jenkins, Travis CI, GitHub Actions, etc. rather than creating API endpoints using FastAPI. 
Setting up a deployment pipeline usually involves configuring your codebase with a CI/CD tool to automatically build, test and deploy your code whenever changes are pushed to the repository. This isn't something that could be achieved by writing Python code or setting up FastAPI endpoints.

However, if you want to provide endpoints to trigger some CI/CD operations, you can do that. Here is an example:

```python
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

# Pydantic Models
class DeploymentModel(BaseModel):
    ci: bool = True
    cd: bool = True

# OAuth2 security scheme instance
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

@app.post("/deploy", response_model=DeploymentModel)
async def deploy_pipeline(deployment: DeploymentModel, token: str = Depends(oauth2_scheme)):
    """
    Endpoint to setup deployment pipeline. 
    It receives a POST request with a JSON body containing the configuration parameters for the deployment pipeline.
    """
    # validate token and handle errors
    try:
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # If the token is valid, proceed with the deployment
    # Here you can add the code to trigger the CI/CD operations based on the deployment model
    return deployment
```

In the above code, we define an endpoint `/deploy` to setup a deployment pipeline. We use OAuth2 for authentication and token validation. In the endpoint, we decode the token and validate the user. If the token is invalid, an error is thrown. After validating the token, the deployment operations can be triggered. 

Please note, you would need to replace `"secret"` with your own secret key and `"HS256"` with your own algorithm. The actual deployment operations are not included in this code and depend on your environment and the CI/CD tools you are using.