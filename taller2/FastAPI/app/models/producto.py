from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    name: str
    price: float
    stock: int
