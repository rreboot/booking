from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: str
    phone: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
