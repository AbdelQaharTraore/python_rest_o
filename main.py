from typing import Optional
from fastapi.params import Body
from pydantic import BaseModel
from fastapi import FastAPI
import json, math

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}


class Position(BaseModel):
    x: int
    y: int


class Restaurant():
    nom: str
    position: Position

    def __init__(self, nom, position):
        self.nom = nom
        self.position = position


def calculer_distance(position: Position, restaurant: Restaurant):
    distance = math.sqrt(
        (position.x - restaurant.position["x"]) ** 2
        + (position.y - restaurant.position["y"]) ** 2
    )
    return distance


@app.post("/resto/near_me")
def near_me(position: Position, distance_max: int = Body(...)):
    resultats_resto = []
    with open("restaurants.json") as file_restaurants:
        restaurants = json.load(file_restaurants)
        for restaurant in restaurants:
            resto_nom = restaurant["nom"]
            resto_x = restaurant["position"]["x"]
            resto_y = restaurant["position"]["y"]

            pos = {"x": resto_x, "y": resto_y}
            resto = Restaurant(resto_nom, pos)

            if calculer_distance(position, resto) < distance_max:
                resultats_resto.append(resto)
    return resultats_resto


@app.post("/resto/far_away")
def far_away(position: Position, distance_min: int = Body(...)):
    resultats_resto = []
    with open("restaurants.json") as file_restaurants:
        restaurants = json.load(file_restaurants)
        for restaurant in restaurants:
            resto_nom = restaurant["nom"]
            resto_x = restaurant["position"]["x"]
            resto_y = restaurant["position"]["y"]

            pos = {"x": resto_x, "y": resto_y}
            resto = Restaurant(resto_nom, pos)

            if calculer_distance(position, resto) > distance_min:
                resultats_resto.append(resto)
    return resultats_resto
