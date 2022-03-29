from datetime import timedelta

from sqlalchemy import Column, Integer, Interval, Numeric, String

from booking.database import Base


class Complex(Base):
    __tablename__ = 'complex'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Numeric, default=0)
    interval = Column(Interval, default=timedelta(seconds=1800))
