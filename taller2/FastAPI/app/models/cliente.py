from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    name: str
    address: str
    phone: str