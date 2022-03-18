from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional

class UserCreate(BaseModel):
    name: str
    lastname: str
    username: str
    email: EmailStr
    password: str
    birthday: date
    gender: str

class UserOut(BaseModel):
    name: str
    lastname: str
    username: str
    email: EmailStr
    birthday: date
    gender: str
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

class PostBase(BaseModel):
    caption: str
    content: str

class PostOut(PostBase):
    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    vote_type: str