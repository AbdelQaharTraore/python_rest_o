from pydantic import BaseModel
from .position import Position
class Restaurant():
    nom: str
    position: Position

    def __init__(self, nom, position):
        self.nom = nom
        self.position = position
