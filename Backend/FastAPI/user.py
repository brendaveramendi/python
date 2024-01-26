from typing import Union
from fastapi import FastAPI, HTTPException
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


@app.get("/users")
async def usersjson():
  return users_list

@app.get("/user/{id}") #Path
async def user(id:int):
  #Filter me devuelve un objeto de tipo iterador
  users = filter(lambda user: user.id == id,users_list)
  print(users)
  return list(users)[0]

@app.get("/user/") #Query
async def user(id:int):
  return search_user(id)

def search_user(id: int):
  users = filter(lambda user: user.id == id, users_list)
  try:
    return list(users)[0]
  except:
    return{"erro":"Usuario excistente"}
#POST
@app.post("/user/",response_model=User,status_code=201) #Query
async def user(user: User):
  if type(search_user(user.id))==User:
    return HTTPException(204,detail="El usuario ya existe")
  else:
    users_list.append(user)

#PUT
#Se usa cuando se actualiza el objeto completo
#PUTH se usa cuando se actualiza un atributo del objeto
@app.put("/user/")
async def user(user:User):
  for index, saved_user in enumerate(users_list):
    if saved_user.id == user.id:
      users_list[index] = user
      return user
    else:
      return {"Error":"No se  ha encontrado el ususario"}

@app.delete("/user/{id}")
async def user(id:int):
  for index, saved_user in enumerate(users_list):
    if saved_user.id == id:
      del users_list[index]
