Sure, below is an example of how you can implement a user authentication API using FastAPI and JWT for token authentication. 

Firstly, let's define our Pydantic user models:

```python
from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True
```

The `UserBase` model contains common attributes for a user. `UserCreate` is used when creating a new user and `User` is used when interacting with existing users.

Now, let's define our service layer:

```python
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
```

Finally, let's implement the API endpoints:

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Any

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/", response_model=User)
def create_user(user: UserCreate):
    # Here you would add the user to the database
    # But for this example, we'll just fake it
    user_in_db = UserInDB(**user.dict())
    user_in_db.hashed_password = get_password_hash(user_in_db.hashed_password)
    fake_users_db[user_in_db.email] = user_in_db
    return user_in_db
```

Here, `/token` endpoint is used for user login. It uses `OAuth2PasswordRequestForm` which provides a `username` and `password`. If the `username` and `password` are correct, it will return an access token.

The `/users/` endpoint is used to create a new user. It receives a `UserCreate` model, hashes the password, and stores the user in the database.

Please note that this is a basic example and doesn't include all the necessary parts you might need in a real-world application, such as database interaction, email confirmation, and more.