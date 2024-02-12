from datetime import timedelta

from app.core.config import settings
from app.dependencies import get_user_service
from app.interfaces.users import IUserService
from app.schemas.users import Token, UserRegistrationData
from app.utils.security import JWTBearer, create_access_token
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing_extensions import Annotated

security_router = APIRouter()


@security_router.post('/login')
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_service: Annotated[IUserService, Depends(get_user_service)]
) -> Token:
    user = await user_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    access_token_expires = timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type='bearer')


@security_router.post('/register')
async def register(
    form_data: UserRegistrationData,
    user_service: Annotated[IUserService, Depends(get_user_service)]
) -> Token:
    new_user = await user_service.add_user(form_data)
    access_token_expires = timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': new_user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type='bearer')


@security_router.post('/test', dependencies=[Depends(JWTBearer())])
async def test():
    return {'siema': 1}
