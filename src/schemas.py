from pydantic import BaseModel
from typing import List, Optional
from pydantic import ConfigDict

class CarBase(BaseModel):
    make: str
    model: str
    year: int
    price: float

class CarCreate(CarBase):
    pass

class Car(CarBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class CarUpdate(BaseModel):
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    price: Optional[float] = None

class CarResponse(CarBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class CarListResponse(BaseModel):
    cars: List[CarResponse]