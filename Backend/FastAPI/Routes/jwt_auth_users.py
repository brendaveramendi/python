from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
ALGORTITHM = "HS256"
app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")
crypt = CryptContext(schemes=["bcrypt"])
ACCESS_TOKEN_DURATION = 1

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
    "password": "$2a$12$QlJyLdlPrOEPsBdyuT.5befhux6qA9hfQn5NHZKLLdOuisipAscMi"#12345
  },
   "maurodev": {
    "username": "maurodev",
    "full_name": "Brains Moure ",
    "email": "brainsmoure@gmail.com",
    "disable": True,
    "password": "$2a$12$QlJyLdlPrOEPsBdyuT.5befhux6qA9hfQn5NHZKLLdOuisipAscMi"
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


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    user = search_user_db(form.username)
    
    
    if not crypt.verify(form.password,user.password):
     raise HTTPException(
       status_code=status.HTTP_400_BAD_REQUEST, detail = "contraseña incorrecta")
     return {"acces_token":user.username,"token_type":"bearer"}
   

