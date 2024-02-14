from collections import defaultdict
from datetime import timedelta

from app.db.models.parking import (ParkingRating, ParkingReservation,
                                   ParkingSpace)
from app.interfaces.parking import IParkingService
from app.schemas.parking import (ParkingSpaceForm, ParkingSpaceInformation,
                                 Position, RatingForm, ReservationForm,
                                 ReservationInformation)
from fastapi import HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession


def _convert_rating(rating: float) -> str:
    if not rating:
        return '0%'
    _rating = rating / 5 * 100
    return f'{_rating:.0f}%'


class ParkingService(IParkingService):
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def _get_parking_spaces_ratings(self) -> dict[int, float]:
        q = select(
            ParkingRating.space_id,
            func.avg(ParkingRating.rating)
        ).join(
            ParkingSpace, ParkingSpace.space_id == ParkingRating.space_id
        ).group_by(
            ParkingRating.space_id
        )
        result = (await self.db_session.execute(q)).all()

        return {
            _id: rating
            for _id, rating in result
        }

    async def _get_reservations_for_user(self, user_id: int) -> dict[int, list[ParkingReservation]]:
        q = select(
            ParkingReservation
        ).filter(
            ParkingReservation.user_id == user_id,
            ParkingReservation.reservation_datetime >= func.now() + timedelta(seconds=15)
        )
        result = await self.db_session.scalars(q)

        result_dict: defaultdict[int, list[ParkingReservation]] = defaultdict(list)
        for reservation in result:
            result_dict[reservation.space_id].append(ReservationInformation(
                reservation_id=reservation.reservation_id,
                reservation_datetime=reservation.reservation_datetime
            ))

        return dict(result_dict)

    async def get_parking_spaces_for_user(self, user_id: int) -> list[ParkingSpaceInformation]:
        result = await self.db_session.scalars(select(ParkingSpace))
        ratings = await self._get_parking_spaces_ratings()
        user_reservations = await self._get_reservations_for_user(user_id)
        return [
            ParkingSpaceInformation(
                space_id=space.space_id,
                position=Position(lat=space.latitude, lng=space.longitude),
                average_rating=_convert_rating(ratings.get(space.space_id, 0.0)),
                reservations=user_reservations.get(space.space_id, [])
            )
            for space in result
        ]

    async def add_parking_space(self, form_data: ParkingSpaceForm) -> None:
        async with self.db_session.begin():
            new_space = ParkingSpace(
                latitude=form_data.latitude,
                longitude=form_data.longitude,
                reservation_limit=form_data.reservation_limit
            )
            self.db_session.add(new_space)

    async def add_reservation(self, form_data: ReservationForm, user_id: int) -> None:
        async with self.db_session.begin():
            space = await self.db_session.scalar(
                select(ParkingSpace).filter(ParkingSpace.space_id == form_data.space_id)
            )
            existing_reservations = await self.db_session.scalar(
                select(
                    func.count(ParkingReservation.reservation_id)
                ).filter(
                    ParkingReservation.space_id == form_data.space_id,
                    ParkingReservation.reservation_datetime >= func.now() + timedelta(seconds=15)
                )
            )
            if existing_reservations and existing_reservations == space.reservation_limit:
                raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Not enough space for more reservations.')
            new_reservation = ParkingReservation(
                reservation_datetime=form_data.reservation_datetime.replace(tzinfo=None),
                user_id=user_id,
                space_id=form_data.space_id
            )
            self.db_session.add(new_reservation)

    async def add_rating(self, form_data: RatingForm) -> None:
        async with self.db_session.begin():
            new_rating = ParkingRating(
                rating=form_data.rating,
                space_id=form_data.space_id
            )
            self.db_session.add(new_rating)
