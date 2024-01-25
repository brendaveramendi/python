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

def search_user(id: int):
  users = filter(lambda user: user.id == id, users_list)
  try:
    return list(users)[0]
  except:
    return{"erro":"Usuario excistente"}

@app.post("/user/")
async def user(user: User):
  if type(search_user(user.id))==User:
    print(users_list)
    return{"erro":"Usuario excistente"}
  else:
    users_list.append(user)

