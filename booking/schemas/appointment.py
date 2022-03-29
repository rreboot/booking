from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AppointmentCreate(BaseModel):
    name: str
    description: Optional[str]
    scheduled_at: datetime


class Appointment(AppointmentCreate):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    user_id: int

    class Config:
        orm_mode = True
