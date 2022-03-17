from pydantic import BaseModel, EmailStr
from datetime import datetime, date

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

class PostBase(BaseModel):
    caption: str
    content: str

class PostOut(PostBase):
    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass
