from sqlalchemy import Column, DateTime, String

from app.database import Base


class Flight(Base):
    __tablename__ = "flights"
    flight_no = Column(String(10), primary_key=True, index=True)
    airline = Column(String(50), nullable=False)
    departure_city = Column(String(50), nullable=False)
    arrival_city = Column(String(50), nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)
