from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
import uvicorn
from dotenv import load_dotenv
from auth import create_access_token, get_password_hash, verify_password
from database import USERS_COLLECTION
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


@app.post("/api/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = USERS_COLLECTION.find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")
    
    access_token = create_access_token(data={"sub": user["username"], "role": user["role"]}, expires_delta=timedelta(hours=1))
    return {"access_token": access_token, "token_type": "bearer"}



# Ejecutar con Uvicorn si se ejecuta directamente
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
