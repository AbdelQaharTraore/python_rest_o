from fastapi.params import Body
from fastapi import FastAPI

from .models.position import Position
from .models.restaurant import Restaurant

import json
import math

app = FastAPI()
file_restaurants = open("restaurants.json", "r")
restaurants = json.load(file_restaurants)


@app.get("/")
def read_root():
    return {"msg": "FastAPI Restaurant"}


@app.post("/resto/near_me")
def near_me(position: Position, distance_max: int = Body(...)):
    resultats_resto = []

    for restaurant in restaurants:
        resto = Restaurant(restaurant["nom"], {
                           "x": restaurant["position"]["x"],
                           "y": restaurant["position"]["y"]
                           })

        if calculer_distance(position, resto) < distance_max:
            resultats_resto.append(resto)

    return resultats_resto


@app.post("/resto/far_away")
def far_away(position: Position, distance_min: int = Body(...)):
    resultats_resto = []

    for restaurant in restaurants:
        resto = Restaurant(restaurant["nom"], {
                           "x": restaurant["position"]["x"],
                           "y": restaurant["position"]["y"]
                           })

        if calculer_distance(position, resto) > distance_min:
            resultats_resto.append(resto)

    return resultats_resto


def calculer_distance(position: Position, restaurant: Restaurant):
    distance = math.sqrt(
        (position.x - restaurant.position["x"]) ** 2
        + (position.y - restaurant.position["y"]) ** 2
    )

    return distance
