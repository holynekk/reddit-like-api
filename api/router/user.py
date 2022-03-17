from fastapi import APIRouter, Depends, status, HTTPException, Response
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
