from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Email(BaseModel):
    fistName: str
    lastName: str
    email: EmailStr
    message : str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/emails/{email_id}")
def read_item(email_id: int):
    return {"email_id": email_id}


@app.put("/emails/{email_id}")
def update_item(email_id: int, email: Email):
    return { "email_id": email_id}