from abc import ABC, abstractmethod

from app.db.models.parking import ParkingSpace
from app.schemas.parking import ParkingSpaceForm, RatingForm, ReservationForm


class IParkingService(ABC):
    @abstractmethod
    async def get_parking_spaces_for_user(self, user_id: int) -> list[ParkingSpace]:
        ...

    @abstractmethod
    async def add_parking_space(self, form_data: ParkingSpaceForm) -> None:
        ...

    @abstractmethod
    async def add_reservation(self, form_data: ReservationForm, user_id: int) -> None:
        ...

    @abstractmethod
    async def add_rating(self, form_data: RatingForm) -> None:
        ...
