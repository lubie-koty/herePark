from datetime import datetime

from app.db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ParkingSpace(Base):
    __tablename__ = 'spaces'

    space_id: Mapped[int] = mapped_column(primary_key=True)
    latitude: Mapped[float]
    longitude: Mapped[float]
    reservation_limit: Mapped[int]

    reservations: Mapped[list['ParkingReservation']] = relationship()
    ratings: Mapped[list['ParkingRating']] = relationship()


class ParkingReservation(Base):
    __tablename__ = 'reservations'

    reservation_id: Mapped[int] = mapped_column(primary_key=True)
    reservation_datetime: Mapped[datetime]
    active: Mapped[bool] = mapped_column(default=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    space_id: Mapped[int] = mapped_column(ForeignKey('spaces.space_id'))


class ParkingRating(Base):
    __tablename__ = 'ratings'

    rating_id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int]

    space_id: Mapped[int] = mapped_column(ForeignKey('spaces.space_id'))
