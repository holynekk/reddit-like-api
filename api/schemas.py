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

class Post(PostBase):
    id: int
    created_at: datetime
    owner_username: str
    owner: UserOut

    class Config:
        orm_mode=True

class PostOut(BaseModel):
    Post: Post
    upvotes: int
    downvotes: int
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

class Follow(BaseModel):
    following_username: str
