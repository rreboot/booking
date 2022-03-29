from booking.api.api_v1.routers import auth
from fastapi import APIRouter

api_router = APIRouter()
# api_router.include_router(recipe.router, prefix="/recipes", tags=["recipes"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
