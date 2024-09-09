from fastapi import APIRouter, Body
from ..models.producto import Producto

producto_route = APIRouter()

@producto_route.get("/")
async def get_productos():
    try:
        return {"message": "Get Product data"}
    except Exception as e:
        return {"error": str(e)}

@producto_route.post("/")
async def post_producto(producto: Producto = Body(...)):
    try:
        return {"message": "Product Created"}
    except Exception as e:
        return {"error": str(e)}

@producto_route.put("/")
async def put_producto():
    try:
        return {"message": "Product Updated"}
    except Exception as e:
        return {"error": str(e)}

@producto_route.delete("/")
async def delete_producto():
    try:
        return {"message": "Product Deleted"}
    except Exception as e:
        return {"error": str(e)}
