from pydantic import BaseModel

class Factura(BaseModel):
    id: int
    date: str
    client_id: int
    total: float