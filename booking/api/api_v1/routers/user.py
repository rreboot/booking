from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from booking import crud, schemas
from booking.api.deps import get_current_user, get_db

router = APIRouter()


@router.get('/users/', response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/me", response_model=schemas.User)
def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    user = current_user
    return user
