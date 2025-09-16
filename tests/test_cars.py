import pytest
from fastapi.testclient import TestClient
from src.main import app
from .settings_tests import client

def test_create_car():
    car_data = {
        "make": "Toyota",
        "model": "Corolla",
        "year": 2022,
        "price": 90000
    }
    response = client.post("/cars/", json=car_data)
    print(response.json())
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200 or response.status_code == 201
    assert response.json()["make"] == "Toyota"
    assert response.json()["model"] == "Corolla"

def test_read_cars():
    response = client.get("/cars/")
    print(response.json())
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_car_with_id():
    car_data = {
        "make": "Ford",
        "model": "Mustang",
        "year": 2021,
        "price": 120000
    }
    create_response = client.post("/cars/", json=car_data)
    assert create_response.status_code == 200 or create_response.status_code == 201
    car_id = create_response.json()["id"]

    response = client.get(f"/cars/{car_id}")
    assert response.status_code == 200
    assert response.json()["id"] == car_id
    assert response.json()["make"] == "Ford"

def test_read_car_not_found():
    response = client.get("/cars/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Car not found"

def test_update_car():
    car_data = {
        "make": "Chevrolet",
        "model": "Camaro",
        "year": 2020,
        "price": 110000
    }
    create_response = client.post("/cars/", json=car_data)
    assert create_response.status_code == 200 or create_response.status_code == 201
    car_id = create_response.json()["id"]

    update_data = {
        "make": "Chevrolet",
        "model": "Camaro SS",
        "year": 2021,
        "price": 115000
    }
    response = client.put(f"/cars/{car_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["model"] == "Camaro SS"
    assert response.json()["year"] == 2021
    assert response.json()["price"] == 115000

def test_update_car_not_found():
    update_data = {
        "make": "Honda",
        "model": "Civic",
        "year": 2023,
        "price": 95000
    }
    response = client.put("/cars/99999", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Car not found"

def test_delete_car():
    car_data = {
        "make": "Nissan",
        "model": "Altima",
        "year": 2019,
        "price": 85000
    }
    create_response = client.post("/cars/", json=car_data)
    assert create_response.status_code == 200 or create_response.status_code == 201
    car_id = create_response.json()["id"]

    response = client.delete(f"/cars/{car_id}")
    assert response.status_code == 200
    assert response.json()["id"] == car_id

    get_response = client.get(f"/cars/{car_id}")
    assert get_response.status_code == 404

def test_delete_car_not_found():
    response = client.delete("/cars/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Car not found"
