from datetime import datetime

from pydantic import BaseModel


class Position(BaseModel):
    lat: float
    lng: float


class ReservationInformation(BaseModel):
    reservation_id: int
    reservation_datetime: datetime


class ParkingSpaceInformation(BaseModel):
    space_id: int
    position: Position
    average_rating: str
    reservations: list[ReservationInformation]


class ParkingSpaceForm(BaseModel):
    latitude: float
    longitude: float
    reservation_limit: int


class ReservationForm(BaseModel):
    space_id: int
    reservation_datetime: datetime


class RatingForm(BaseModel):
    space_id: int
    rating: int
