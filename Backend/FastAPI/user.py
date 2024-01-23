from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


#Entidad user
#Base model me da la capaciadad
#De crear una entidad
class User(BaseModel):
  id: int
  name: str
  apellido: str

users_list = [User(id=1, name="Pamela",apellido="Veramendi"),User(id=2, name="Rebeca",apellido="Veramendi"),User(id=3,name="Brenda",apellido="Veramendi")]


@app.get("/usersjson")
async def usersjson():
  return [{"name":"Brenda","Apellido":"Veramendi"},{"name":"Rebeca","Apellido":"Veramendi"}]

@app.get("/user/{id}")
async def user(id:int):
  #Filter me devuelve un objeto de tipo iterador
  users = filter(lambda user: user.id == id,users_list)
  print(users)
  return list(users)
