from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from booking import crud, schemas
from booking.api.deps import get_db

router = APIRouter()


@router.post('/appointments/', response_model=schemas.Appointment)
def create_appointment(
    appointment: schemas.AppointmentCreate,
    user_id: Optional[int],
    db: Session = Depends(get_db)
):
    return crud.create_appointment(db, appointment, user_id)


@router.get('/appointments/', response_model=list[schemas.Appointment])
def read_appointments(db: Session = Depends(get_db)):
    appointments = crud.get_appointments(db)
    return appointments
