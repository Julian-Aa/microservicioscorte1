from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Routers importados desde la carpeta routes
from .routes.cliente import client_route
from .routes.producto import producto_route
from .routes.transaccion import transaccion_route
from .routes.veterinario import veterinario_route
from .routes.factura import factura_route


app = FastAPI()

# Redirección a la documentación por defecto
@app.get("/")
async def docs():
    return RedirectResponse(url="/docs")



app.include_router(client_route, prefix="/clientes", tags=["Clientes"])
app.include_router(producto_route, prefix="/productos", tags=["Productos"])
app.include_router(transaccion_route, prefix="/transacciones", tags=["Transacciones"])
app.include_router(veterinario_route, prefix="/veterinario", tags=["Veterinario"])
app.include_router(factura_route, prefix="/facturas", tags=["Facturas"])
