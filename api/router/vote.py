from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(prefix="/votes", tags=["Vote"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote_post(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user : str = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {vote.post_id} was not found")
    vote_query = db.query(models.Vote).filter(models.Vote.post_id==vote.post_id, models.Vote.username==current_user.username)
    found_vote = vote_query.first()

    # If there is already a vote
    if found_vote:
        # If user tries to remove their vote by pressing the same button
        if found_vote.vote_type == vote.vote_type:
            vote_query.delete(synchronize_session=False)
            db.commit()
        # Else user change his/her vote from downvote to upvote or vice versa (vote_type should be valid)
        elif vote.vote_type == "upvote" or vote.vote_type == "downvote":
            vote_query.update(vote.dict(), synchronize_session=False)
            db.commit()
    # Else there is no vote and vote_type is valid
    elif vote.vote_type == "upvote" or vote.vote_type == "downvote":
        new_vote = models.Vote(post_id=vote.post_id, vote_type=vote.vote_type, username=current_user.username)
        db.add(new_vote)
        db.commit()
        return {"message": "Vote successfully added"}
    else:
        pass
    pass
