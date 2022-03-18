from sqlalchemy import TIMESTAMP, Column, String, Integer, Date, ForeignKey
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

class Vote(Base):
    __tablename__ = "votes"

    username = Column(String, ForeignKey("users.username", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    vote_type = Column(String, nullable=False)
