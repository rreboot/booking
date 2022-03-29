from typing import Optional
from sqlalchemy.orm import Session

from booking import models, schemas


def get_appointment(db: Session, appointment_id: int):
    return db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()


def get_appointments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Appointment).offset(skip).limit(limit).all()


def create_appointment(db: Session, appointment: schemas.AppointmentCreate, user_id: int):
    user_id: int
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
