from pydantic import BaseModel, EmailStr


class EmailBase(BaseModel):
    fistName: str
    lastName: str
    email: EmailStr
    message : str

class EmailCreate(BaseModel):
    pass

class Email(EmailBase):
    id: int
    class Config:
        orm_mode = True