from multiprocessing import synchronize
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from sqlalchemy import func, case
from typing import List
from ..database import get_db
from .. import models, schemas, oauth2

router = APIRouter(prefix="/follows", tags=['Follows'])

# Get Followers
@router.get('/{username}', response_model=List[schemas.UserOut])
def get_all_followers(username: str, db: Session = Depends(get_db)):
    all_followers = db.query(models.User).join(models.Follow, models.Follow.follower_username==models.User.username, isouter=True).filter(models.User.username == models.Follow.follower_username).all()
    return all_followers

# Follow User
@router.post('/{following_username}', status_code=status.HTTP_201_CREATED)
def follow_user(following_username: str, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    already_follows = db.query(models.Follow).filter(models.Follow.following_username==following_username, current_user.username==models.Follow.follower_username).first()
    if already_follows:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User {current_user.username} already follows {following_username}")
    following_user = db.query(models.User).filter(models.User.username==following_username).first()
    if not following_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with username {following_username} was not found")
    follow_user = models.Follow(follower_username=current_user.username, following_username=following_username)
    db.add(follow_user)
    db.commit()
    db.refresh(follow_user)
    return follow_user

# Unfollow user
@router.delete('/{following_username}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(following_username: str, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    is_following_query = db.query(models.Follow).filter(models.Follow.following_username==following_username)
    is_following_object = is_following_query.first()
    if is_following_object:
        is_following_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with username {current_user.username} is not following user {following_username}")
