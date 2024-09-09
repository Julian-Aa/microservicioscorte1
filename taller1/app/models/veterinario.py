from pydantic import BaseModel

class Veterinario(BaseModel):
    id: int
    name: str
    specialty: str
    years_experience: int
