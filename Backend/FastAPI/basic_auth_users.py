from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
  username: str
  full_name: str
  email: str
  disable: bool

class UserDB(User):
  password: str
  
users_db = {
  "brendadev": {
    "username": "brendaveramendi",
    "full_name": "Brenda Veramendi",
    "email": "brendaveramendi@gmail.com",
    "disable": False,
    "password": "12345"
  },
   "maurodev": {
    "username": "maurodev",
    "full_name": "Brains Moure ",
    "email": "brainsmoure@gmail.com",
    "disable": True,
    "password": "12345"
  }
}
def search_user_db(username: str):
  if username in users_db:
    #El asterisco es multiples parametros
    return UserDB(**users_db[username])
  
def search_user(username: str):
  if username in users_db:
    #El asterisco es multiples parametros
    return User(**users_db[username])


async def current_user(token: str = Depends(oauth2)):
  user = search_user(token)
  if not user:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales invalidas", headers={"WWW-Authenticate":"Beare"})
  if user.disable:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario Inactivo")
  return user   

#depens recibe datos pero no depemnde de nadie  

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
   user_db = form.username 
   if not user_db:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
   
   user = search_user_db(form.username)
   print("---->",user)
   if not form.password == user.password:
     raise HTTPException(
       status_code=status.HTTP_400_BAD_REQUEST, detail = "contraseña incorrecta")
   return {"acces_token":user.username,"token_type":"bearer"}
 
@app.get("/users/me")
async def me(user: User = Depends(current_user)):
  return user


 