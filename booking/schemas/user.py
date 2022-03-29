from typing import Optional

from pydantic import BaseModel

from booking.schemas.appointment import Appointment


class UserBase(BaseModel):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    appointments: list[Appointment] = []

    class Config:
        orm_mode = True
