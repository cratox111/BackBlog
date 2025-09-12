from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import APIRouter, HTTPException, status
from passlib.context import CryptContext
from jose import jwt
from db.schemas import model_user
from db.client import users

router = APIRouter(prefix='/auth', tags=['Auth user'])

oauth = OAuth2PasswordBearer(tokenUrl='auth/login')
crypt = CryptContext(schemes=['bcrypt'])
SECRET = 'fdsfsdfgdgdfhgfhnhgjhgmjk'

def shear_user(key, value):
    user = users.find_one({key: value})
    if not user:
        return False
    return user

@router.post('/register')
async def register(user: model_user.UserForm):
    if shear_user(key='username', value=user.username) or shear_user(key='email', value=user.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User existente'
        )
    
    user.password = crypt.hash(user.password)
    
    user_dict = dict(user)
    users.insert_one(user_dict).inserted_id

    return {'msg':'User creado'}