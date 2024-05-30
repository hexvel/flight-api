from datetime import datetime

from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.auth import verify_api_key
from app.database import get_db
from app.models import Flight

router = APIRouter()


class FlightCreate(BaseModel):
    flight_no: str
    airline: str
    departure_city: str
    arrival_city: str
    departure_time: datetime
    arrival_time: datetime


class FlightResponse(BaseModel):
    flight_no: str
    airline: str
    departure_city: str
    arrival_city: str
    departure_time: datetime
    arrival_time: datetime


@router.post("/api/v1/flights", response_model=dict)
def add_flight(
    flight: FlightCreate, db: Session = Depends(get_db), x_api_key: str = Header(None)
):
    verify_api_key(x_api_key)
    db_flight = Flight(
        flight_no=flight.flight_no,
        airline=flight.airline,
        departure_city=flight.departure_city,
        arrival_city=flight.arrival_city,
        departure_time=flight.departure_time,
        arrival_time=flight.arrival_time,
    )
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return {"message": "Flight added successfully"}


# @router.get("/api/v1/flights", response_model=list[FlightResponse])
# def get_all_flights(db: Session = Depends(get_db), x_api_key: str = Header(None)):
#     verify_api_key(x_api_key)
#     flights = db.query(Flight).all()
#     return flights


@router.get("/api/v1/flights/{flight_no}", response_model=FlightResponse)
def get_flight(
    flight_no: str, db: Session = Depends(get_db), x_api_key: str = Header(None)
):
    verify_api_key(x_api_key)
    flight = db.query(Flight).filter(Flight.flight_no == flight_no).first()
    if flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    return {
        "flight_no": flight.flight_no,
        "airline": flight.airline,
        "departure_city": flight.departure_city,
        "arrival_city": flight.arrival_city,
        "departure_time": flight.departure_time,
        "arrival_time": flight.arrival_time,
    }
