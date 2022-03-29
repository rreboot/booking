from datetime import timedelta

from pydantic import BaseModel


class ComplexCreate(BaseModel):
    name: str
    description: str
    price: float
    interval: timedelta


class Complex(ComplexCreate):
    id: int

    class Config:
        orm_mode = True
