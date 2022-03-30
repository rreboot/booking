from fastapi import APIRouter, FastAPI

from booking.api.api_v1.api import api_router

root_router = APIRouter()
app = FastAPI(title='Booking API')


@root_router.get('/', tags=['root'])
async def root():
    return {'message': 'Hello World'}

app.include_router(api_router)
app.include_router(root_router)
