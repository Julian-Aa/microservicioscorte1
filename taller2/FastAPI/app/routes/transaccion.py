from fastapi import APIRouter, Body
from ..models.transaccion import Transaccion

transaccion_route = APIRouter()

@transaccion_route.get("/")
async def get_transacciones():
    try:
        return {"message": "Get Transaccion data"}
    except Exception as e:
        return {"error": str(e)}

@transaccion_route.post("/")
async def post_transaccion(transaccion: Transaccion = Body(...)):
    try:
        return {"message": "Transaccion Created"}
    except Exception as e:
        return {"error": str(e)}

@transaccion_route.put("/")
async def put_transaccion():
    try:
        return {"message": "Transaccion Updated"}
    except Exception as e:
        return {"error": str(e)}

@transaccion_route.delete("/")
async def delete_transaccion():
    try:
        return {"message": "Transaccion Deleted"}
    except Exception as e:
        return {"error": str(e)}
