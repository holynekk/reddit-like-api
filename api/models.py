from sqlalchemy import TIMESTAMP, Column, String, Integer, Date
from sqlalchemy.sql.expression import text
from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    caption =  Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class User(Base):
    __tablename__ = "users"
    
    username = Column(String, primary_key=True, nullable=False)
    name =  Column(String, nullable=False)
    lastname =  Column(String, nullable=False)
    email =  Column(String, nullable=False)
    password =  Column(String, nullable=False)
    birthday = Column(Date, nullable=False)
    gender =  Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

