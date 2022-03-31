from sqlalchemy.orm import Session

from booking import models, schemas
from booking.auth.base import get_password_hash


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    user_data = user.dict()
    password = user_data.pop('password')

    db_user = models.User(**user_data)
    db_user.hashed_password = get_password_hash(password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
