from typing import Optional

from fastapi import FastAPI
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/emails/")
def create_email(email : schemas.EmailCreate, db: Session = Depends(get_db)):
    pass

