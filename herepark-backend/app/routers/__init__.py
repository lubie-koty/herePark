from app.routers.security import security_router
from fastapi import APIRouter

main_router = APIRouter()
main_router.include_router(security_router, prefix='/security')
