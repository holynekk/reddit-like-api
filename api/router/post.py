from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models, schemas, oauth2

router = APIRouter(prefix="/posts", tags=['Posts'])

# Get posts
@router.get('/', response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db)):
    all_posts = db.query(models.Post).all()
    return all_posts

@router.get('/{id}', response_model=schemas.PostOut)
def get_posts(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found!")
    return post

# Create posts
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    created_post = models.Post(**post.dict())
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return created_post

# Update post
@router.put("/{id}", response_model=schemas.PostOut)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db) , current_user: str = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id==id)
    
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found!")
    post.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post.first()

# Delete Post
@router.post('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    print(id)
    post = db.query(models.Post).filter(models.Post.id==id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found!")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
