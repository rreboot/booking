from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy import or_
from sqlalchemy.orm import Session

from booking import models
from booking.auth.base import oauth2_scheme
from booking.auth.models import TokenData
from booking.database import SessionLocal
from booking.settings import settings


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = db.query(models.User).filter(
        or_(models.User.username == token_data.username, models.User.email == token_data.username)
    ).first()

    if user is None:
        raise credentials_exception
    return user


# async def get_current_active_user(current_user: schemas.User = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user
