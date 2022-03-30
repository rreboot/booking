from fastapi import APIRouter

from booking.api.api_v1.routers import appointment, auth, complex, user

api_router = APIRouter()
# api_router.include_router(recipe.router, prefix='/recipes', tags=['recipes'])
api_router.include_router(auth.router, prefix='/auth', tags=['auth'])
api_router.include_router(appointment.router, tags=['appointment'])
api_router.include_router(complex.router, tags=['complex'])
api_router.include_router(user.router, tags=['user'])
