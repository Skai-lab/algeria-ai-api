from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base



class Email(Base):
    __tablename__ = "emails"

    id =  Column(Integer, primary_key=True, index=True)
    fistName: Column(Integer)
    lastName: Column(Integer, primary_key=True, index=True)
    email: Column(Integer, primary_key=True, index=True)
    message : Column(Integer, primary_key=True, index=True)