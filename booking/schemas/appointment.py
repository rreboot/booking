from lib2to3.pytree import Base
from pydantic import BaseModel


class Appointment(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
