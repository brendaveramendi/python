from typing import Union
from fastapi import FastAPI
from Routes import products
from Routes import user

app = FastAPI()

# Routes
app.include_router(products.router)
app.include_router(user.router)
@app.get("/")
async def root():
  return "Hola FastAPi"
