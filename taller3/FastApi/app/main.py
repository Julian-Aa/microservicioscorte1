from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Base de datos
from routes.frutas import fruta_route # Cambiado para importar las rutas de frutas

from contextlib import asynccontextmanager
from database import database as connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar la conexión cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

# Rutas
app.include_router(fruta_route, prefix="/frutas", tags=["Frutas"])  # Cambiado para frutas
