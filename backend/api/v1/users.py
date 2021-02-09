from fastapi import APIRouter, Body, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from sqlalchemy.orm import Session

from backend import crud, schemas
from backend.api.dependencies import get_db
from backend.core.config import SECRET_KEY, ALGORITHM

import re

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/token')

@router.post('/api/v1/users/', response_model=schemas.User, tags=['users'])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user.username = user.username.capitalize()
    db_user = crud.get_user_by_username(db, user.username)

    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Username already registered')

    if not re.match(r'\w+\Z', user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Username must only contains: letters, digits and underscore')

    return crud.create_user(db, user)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials, Reason: check the token has not expired', # change
        headers={'WWW-Authenticate': 'Bearer'}
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        
        sub: str = payload.get('sub')
        name: str = payload.get('name')
        exp: int = payload.get('exp')
        
        if sub is None or name is None or exp is None:
            raise credentials_exception

        token_data = schemas.TokenData(sub=sub, name=name, exp=exp)
    except JWTError as e:
        raise credentials_exception
    
    user = crud.get_user_by_username(db, token_data.name)
    
    if user is None:
        raise credentials_exception

    return user


@router.get('/api/v1/users/me', response_model=schemas.User, tags=['users'])
def read_current_user(current_user: schemas.User = Depends(get_current_user)):
    return current_user


@router.put('/api/v1/users/me', response_model=schemas.User, tags=['users'])
def update_password(new_password: str = Body(..., embed=True), current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    return crud.update_password(db, new_password, current_user)


@router.get('/api/v1/users/{username}', response_model=schemas.User, tags=['users'])
def read_user(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username)

    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User not found')

    return db_user
