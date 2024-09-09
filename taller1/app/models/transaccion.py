from pydantic import BaseModel

class Transaccion(BaseModel):
    id: int
    client_id: int
    product_id: int
    quantity: int
    total: float
