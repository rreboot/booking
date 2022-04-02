from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from booking import models, schemas


def get_appointment(db: Session, appointment_id: int):
    return db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()


def get_appointments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Appointment).offset(skip).limit(limit).all()


def appointment_complex_list(db: Session, appointment_id: int):
    appointment: models.Appointment = db.query(models.Appointment).filter(
        models.Appointment.id == appointment_id
    ).first()

    if not appointment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Такой записи не существует'
        )

    return appointment.complex


def create_appointment(db: Session, appointment: schemas.AppointmentCreate, user_id: int):
    db_appointment = models.Appointment(
        name=appointment.name,
        description=appointment.description,
        scheduled_at=appointment.scheduled_at,
        user_id=user_id
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def add_complex(db: Session, appointment_id: int, complex_id: int):
    appointment: models.Appointment = db.query(models.Appointment).filter(
        models.Appointment.id == appointment_id
    ).first()
    complex: models.Complex = db.query(models.Complex).filter(
        models.Complex.id == complex_id
    ).first()
    if not (appointment and complex):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='appointment or complex is None'
        )
    appointment.complex.append(complex)
    db.commit()
    db.refresh(appointment)
    return appointment
