from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from booking.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String, nullable=True)
    phone = Column(String, index=True)
    email = Column(String, unique=True, nullable=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    appointment = relationship('Appointment', backref='user')
