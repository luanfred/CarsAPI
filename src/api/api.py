from .endpoins import cars
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(cars.router, prefix="/cars", tags=["Carros"])
