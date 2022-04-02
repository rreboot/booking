from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from booking import crud, schemas
from booking.api.deps import get_db

router = APIRouter()


@router.post('/appointment/', response_model=schemas.Appointment)
def create_appointment(
    appointment: schemas.AppointmentCreate,
    user_id: Optional[int],
    db: Session = Depends(get_db)
):
    return crud.create_appointment(db, appointment, user_id)


@router.post(
    '/appointment/{appointment_id}/complex/{complex_id}', response_model=schemas.Appointment
)
def add_complex(appointment_id: int, complex_id: int, db: Session = Depends(get_db)):
    return crud.add_complex(db, appointment_id, complex_id)


@router.get('/appointments/', response_model=list[schemas.Appointment])
def read_appointments(db: Session = Depends(get_db)):
    appointments = crud.get_appointments(db)
    return appointments


@router.get('/appointment/{appointment_id}/complex/', response_model=list[schemas.Complex])
def read_appointment_complex_list(appointment_id: int, db: Session = Depends(get_db)):
    return crud.appointment_complex_list(db, appointment_id)
