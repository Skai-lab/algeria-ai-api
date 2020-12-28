from pydantic import BaseModel, EmailStr


class EmaiBase(BaseModel):
    fistName: str
    lastName: str
    email: EmailStr
    message : str

class Email(EmailBase):
    id: int
    class Config:
        orm_mode = True