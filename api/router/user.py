from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models, schemas, utils

router = APIRouter(prefix="/users", tags=['User'])

# Create Users
@router.post('/', response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user_info: schemas.UserCreate, db: Session = Depends(get_db)):
    user_info.password = utils.hash(user_info.password)
    new_user = models.User(**user_info.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get User
@router.get('/{username}', response_model=schemas.UserOut)
def get_user(username: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username==username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with username: {username} was not found")
    return user