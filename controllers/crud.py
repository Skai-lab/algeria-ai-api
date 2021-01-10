from sqlalchemy.orm import Session
from models import models, schemas


def get_email(db: Session, email_id: int):
    return db.query(models.Email).filter(models.Email.id == email_id).first()

def get_emails(db :  Session):
    return db.query(models.Email).all()
    
def create_email(db: Session, email: schemas.EmailCreate):
    db_email = models.Email(first_name=email.firstName, last_name= email.lastName, email= email.email, text= email.text)
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email