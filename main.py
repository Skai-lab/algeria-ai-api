from typing import Optional
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
import controllers as crud, models, config
from config.database import SessionLocal, engine

config.Base.metadata.create_all(bind=engine)
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


@app.post("/emails/create/")
def create_email(email : models.EmailCreate, db: Session = Depends(get_db)):
    pass


@app.get("/emails/list/")
def list_emails( db: Session = Depends(get_db)):
    return crud.get_emails(db)


