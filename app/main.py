from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from dotenv import load_dotenv
load_dotenv()

import os
VERSION = "0.0.1"
STAGE = os.environ["STAGE"]
COFFEE_SHOP = os.environ["COFFEE_SHOP"]

# Importar rutas (una vez que las tengas)
from routes import product #, sale, expense

# Crear la aplicación FastAPI
app = FastAPI()

# Incluir rutas en la aplicación
app.include_router(product.router, prefix="/api/products", tags=["Products"])
#app.include_router(sale.router, prefix="/api/sales", tags=["Sales"])
#app.include_router(expense.router, prefix="/api/expenses", tags=["Expenses"])

# Servir archivos estáticos (para frontend si lo tienes en "static")
#app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta de prueba
@app.get("/")
async def root():
    return {"message": f"Bienvenido a la API de la cafetería: {COFFEE_SHOP}",
            "stage":STAGE,
            "version":VERSION}

# Ejecutar con Uvicorn si se ejecuta directamente
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
