from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ... import crud, schemas
from ...database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Car)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = crud.create_car(db=db, car=car)
    if db_car is None:
        raise HTTPException(status_code=400, detail="Car could not be created")
    return db_car

@router.get("/", response_model=list[schemas.Car])
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cars = crud.get_cars(db=db, skip=skip, limit=limit)
    return cars

@router.get("/{car_id}", response_model=schemas.Car)
def read_car(car_id: int, db: Session = Depends(get_db)):
    db_car = crud.get_car(db=db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@router.put("/{car_id}", response_model=schemas.Car)
def update_car(car_id: int, car: schemas.CarUpdate, db: Session = Depends(get_db)):
    db_car = crud.get_car(db=db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return crud.update_car(db=db, car_id=car_id, car=car)

@router.delete("/{car_id}", response_model=schemas.Car)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = crud.get_car(db=db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return crud.delete_car(db=db, car_id=car_id)