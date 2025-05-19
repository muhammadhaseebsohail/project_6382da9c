Below are the necessary Pydantic models for the provided API endpoints:

```python
from typing import Optional
from pydantic import BaseModel, EmailStr

class TokenData(BaseModel):
    email: Optional[EmailStr] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True
```

The `Token` model is used for the response from the `/token` endpoint, and `TokenData` is used for the data stored in a token. `UserInDB` is used as a data transfer object for handling user data with the hashed password.

Additionally, below are imports for the FastAPI application and all the dependencies used in the service layer and the endpoints:

```python
from typing import Any
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
```

Please note that you would need to replace `"YOUR_SECRET_KEY"` with your actual secret key for JWT generation. Also, `fake_users_db` and `authenticate_user` in the `/token` endpoint are placeholders for your actual user database and authentication function respectively.