from pydantic import BaseModel
from database import database

class Fruta(BaseModel):
    id: int
    nombre: str
    color: str
    peso: float
    origen: str
    precio: float
