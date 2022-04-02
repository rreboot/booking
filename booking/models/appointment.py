from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from booking.database import Base

appointment_complex = Table(
    'appointment_complex',
    Base.metadata,
    Column('appointment_id', ForeignKey('appointments.id'), primary_key=True),
    Column('complex_id', ForeignKey('complex.id'), primary_key=True)
)


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    scheduled_at = Column(DateTime(timezone=True))

    user_id = Column(Integer, ForeignKey('users.id'))
    complex = relationship("Complex", secondary=appointment_complex, backref='appointments')
