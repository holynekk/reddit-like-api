from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    caption: str
    content: str

class PostOut(PostBase):
    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass
