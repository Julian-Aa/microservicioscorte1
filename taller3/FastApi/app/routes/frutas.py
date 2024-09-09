from fastapi import APIRouter, Body, HTTPException
from models.frutas import Fruta

from database import FrutaModel, database

fruta_route = APIRouter()

@fruta_route.get("/")
def get_all_frutas():
    try:
        frutas = FrutaModel.select()  # Obtén todas las frutas
        # Convierte las frutas a un formato serializable
        fruta_list = [{
            "id": fruta.id,
            "nombre": fruta.nombre,
            "color": fruta.color,
            "peso": fruta.peso,
            "origen": fruta.origen,  # Asegúrate de que el nombre del campo es correcto
            "precio": fruta.precio
        } for fruta in frutas]
        return fruta_list
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@fruta_route.get("/{frutaId}")
def get_fruta(frutaId: int):
    try:
        fruta = FrutaModel.get(FrutaModel.id == frutaId)
        return fruta
    except Exception as e:
        print(e)
        return {"error": str(e)}


@fruta_route.post("/frutas")
def create_fruta(fruta: Fruta = Body(...)):
    try:
        database.connect()
        FrutaModel.create(
            nombre=fruta.nombre, 
            color=fruta.color, 
            peso=fruta.peso, 
            origen=fruta.origen, 
            precio=fruta.precio
        )
        return fruta
    except Exception as e:
        print(e)
        return {"error": str(e)}
    finally:
        database.close()  # Asegúrate de cerrar la conexión


@fruta_route.put("/{frutaId}")
def update_fruta(frutaId: int, fruta: Fruta = Body(...)):
    try:
        existing_fruta = FrutaModel.get(FrutaModel.id == frutaId)  # Busca la fruta por ID
        
        # Actualiza los campos de la fruta con los valores del cuerpo de la solicitud
        existing_fruta.nombre = fruta.nombre
        existing_fruta.color = fruta.color
        existing_fruta.peso = fruta.peso
        existing_fruta.origen = fruta.origen
        existing_fruta.precio = fruta.precio
        
        existing_fruta.save()  # Guarda los cambios en la base de datos
        return {"message": "Fruta updated successfully"}
    except FrutaModel.DoesNotExist:
        raise HTTPException(status_code=404, detail="Fruta not found")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@fruta_route.delete("/{frutaId}")
def delete_fruta(frutaId: int):
    try:
        fruta = FrutaModel.get(FrutaModel.id == frutaId)
        fruta.delete_instance()
        return "Fruta borrada"
    except Exception as e:
        print(e)
        return {"error": str(e)}
