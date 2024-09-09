from fastapi import APIRouter, Body
from ..models.factura import Factura

factura_route = APIRouter()

@factura_route.get("/")
async def get_facturas():
    try:
        return {"message": "Get Factura data"}
    except Exception as e:
        return {"error": str(e)}

@factura_route.post("/")
async def post_factura(factura: Factura = Body(...)):
    try:
        return {"message": "Factura Created"}
    except Exception as e:
        return {"error": str(e)}

@factura_route.put("/")
async def put_factura():
    try:
        return {"message": "Factura Updated"}
    except Exception as e:
        return {"error": str(e)}

@factura_route.delete("/")
async def delete_factura():
    try:
        return {"message": "Factura Deleted"}
    except Exception as e:
        return {"error": str(e)}
