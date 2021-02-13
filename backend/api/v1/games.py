from fastapi import APIRouter, Body, Depends, status
from fastapi.exceptions import HTTPException

from sqlalchemy.orm import Session

from typing import List

from backend import crud, schemas
from backend.api.dependencies import get_current_user, get_db

import re

router = APIRouter()

@router.get('/api/v1/games/', response_model=List[schemas.Game], tags=['games'])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_games(db, skip=skip, limit=limit)
    return users


@router.post('/api/v1/users/me/games/', response_model=schemas.Game, tags=['games'])
def create_game(game: schemas.GameCreate, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    game.name = game.name.capitalize()
    game.name = game.name.strip()
    game.name = re.sub(' +', ' ', game.name.strip())
    db_game = crud.get_game_by_name(db, game.name, current_user)

    if db_game:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Game already registered')

    if not re.match(r'[\w ]+\Z', game.name):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Game name must only contains: letters, digits, spaces or underscore')

    return crud.create_user_game(db, game, current_user.id)


@router.get('/api/v1/users/me/games/', response_model=List[schemas.Game], tags=['games'])
def read_current_user_games(skip: int = 0, limit: int = 100, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    users = crud.get_games_current_user(db, current_user, skip=skip, limit=limit)
    return users


@router.get('/api/v1/users/me/games/{name}', response_model=schemas.Game, tags=['games'])
def read_current_user_game(name: str, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    name = name.capitalize()
    db_game = crud.get_game_by_name(db, name, current_user)

    if db_game is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Game not found')

    return db_game


@router.put('/api/v1/users/me/games/{name}', response_model=schemas.Game, tags=['games'])
def update_current_user_game(name: str, game_update: schemas.GameUpdate, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    name = name.capitalize()
    db_game = crud.get_game_by_name(db, name, current_user)

    if not db_game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Game not found')

    if game_update.new_name:
        game_update.new_name = game_update.new_name.capitalize()

    return crud.update_current_user_game(db, name, game_update, current_user)   


@router.delete('/api/v1/users/me/games/{name}', status_code=status.HTTP_204_NO_CONTENT, tags=['games'])
def delete_current_user_game(name: str, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    name = name.capitalize()
    db_game = crud.get_game_by_name(db, name, current_user)

    if not db_game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Game not found')

    crud.delete_game(db, name, current_user)
