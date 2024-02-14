from app.db.models.users import User
from app.dependencies import get_current_user, get_parking_service
from app.interfaces.parking import IParkingService
from app.schemas.parking import (ParkingSpaceForm, ParkingSpaceInformation,
                                 RatingForm, ReservationForm)
from app.utils.security import JWTBearer
from fastapi import APIRouter, Depends
from typing_extensions import Annotated

parking_router = APIRouter()


@parking_router.get('/parking_spaces')
async def get_parking_spaces_with_reservations(
    parking_service: Annotated[IParkingService, Depends(get_parking_service)],
    current_user: Annotated[User, Depends(get_current_user)]
) -> list[ParkingSpaceInformation]:
    return await parking_service.get_parking_spaces_for_user(current_user.user_id)


@parking_router.post('/parking_spaces', dependencies=[Depends(JWTBearer())])
async def add_parking_space(
    form_data: ParkingSpaceForm,
    parking_service: Annotated[IParkingService, Depends(get_parking_service)]
):
    await parking_service.add_parking_space(form_data)


@parking_router.post('/reservations')
async def add_reservation(
    form_data: ReservationForm,
    parking_service: Annotated[IParkingService, Depends(get_parking_service)],
    current_user: Annotated[User, Depends(get_current_user)]
):
    await parking_service.add_reservation(form_data, current_user.user_id)


@parking_router.post('/ratings', dependencies=[Depends(JWTBearer())])
async def add_rating(
    form_data: RatingForm,
    parking_service: Annotated[IParkingService, Depends(get_parking_service)]
):
    await parking_service.add_rating(form_data)
