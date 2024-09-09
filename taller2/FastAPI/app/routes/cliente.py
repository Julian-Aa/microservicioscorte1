from fastapi import APIRouter, Body
from ..models.cliente import Cliente

client_route = APIRouter()

@client_route.get("/clientes")
async def get_clients():
    try:
        return {"message": "Get Client data"}
    except Exception as e:
        return {"error": str(e)}

@client_route.post("/clientes")
async def post_client(cliente: Cliente = Body(...)):
    try:
        return {"message": "Client Created"}
    except Exception as e:
        return {"error": str(e)}

@client_route.put("/")
async def put_client():
    try:
        return {"message": "Client Updated"}
    except Exception as e:
        return {"error": str(e)}

@client_route.delete("/clientes")
async def delete_client():
    try:
        return {"message": "Client Deleted"}
    except Exception as e:
        return {"error": str(e)}
