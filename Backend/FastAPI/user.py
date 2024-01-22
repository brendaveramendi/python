from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/users")
async def users():
  return [{"name":"Brenda","Apellido":"Veramendi"},{"name":"Rebeca","Apellido":"Veramendi"}]
