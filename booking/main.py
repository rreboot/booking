from typing import Optional

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from booking import crud, schemas
from booking.api.api_v1.api import api_router
from booking.api.deps import get_db

root_router = APIRouter()
app = FastAPI(title='Booking API')


@app.get('/')
async def root():
    return {'message': 'Hello World'}

app.include_router(api_router)
app.include_router(root_router)


@app.get('/users/', response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.post('/appointments/', response_model=schemas.Appointment)
def create_appointment(
    appointment: schemas.AppointmentCreate,
    user_id: Optional[int],
    db: Session = Depends(get_db)
):
    return crud.create_appointment(db, appointment, user_id)


@app.get('/appointments/', response_model=list[schemas.Appointment])
def read_appointments(db: Session = Depends(get_db)):
    appointments = crud.get_appointments(db)
    return appointments


@app.get('/complex_list/', response_model=list[schemas.Complex])
def read_complex_list(db: Session = Depends(get_db)):
    complex_list = crud.get_complex_list(db)
    return complex_list


@app.post('/complex/', response_model=schemas.Complex)
def create_complex(complex: schemas.ComplexCreate, db: Session = Depends(get_db)):
    return crud.create_complex(db, complex)
