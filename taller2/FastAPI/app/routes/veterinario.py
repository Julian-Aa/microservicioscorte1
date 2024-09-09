from fastapi import APIRouter, Body
from ..models.veterinario import Veterinario

veterinario_route = APIRouter()

@veterinario_route.get("/")
async def get_veterinarios():
    try:
        return {"message": "Get Veterinario data"}
    except Exception as e:
        return {"error": str(e)}

@veterinario_route.post("/")
async def post_veterinario(veterinario: Veterinario = Body(...)):
    try:
        return {"message": "Veterinario Created"}
    except Exception as e:
        return {"error": str(e)}

@veterinario_route.put("/")
async def put_veterinario():
    try:
        return {"message": "Veterinario Updated"}
    except Exception as e:
        return {"error": str(e)}

@veterinario_route.delete("/")
async def delete_veterinario():
    try:
        return {"message": "Veterinario Deleted"}
    except Exception as e:
        return {"error": str(e)}
