from fastapi import FastAPI
from .models import Base
from . import models
from .database import engine
from .router import post

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(post.router)

@app.get("/")
def root():
    return {"message": "Hello World"}