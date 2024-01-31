from typing import Union
from fastapi import FastAPI
from Routes import products
from Routes import user
from fastapi.staticfiles import StaticFiles
app = FastAPI()

# Routes
app.include_router(products.router)
app.include_router(user.router)
#1 static como encuentro el recurso
#2 parametro es el directorio
#3 Es como se llama el recurso 
app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/")
async def root():
  return "Hola FastAPi"

