from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from sqlalchemy.orm import Session

from backend import crud, schemas
from backend.api.dependencies import get_db, get_current_user

router = APIRouter()

@router.post('/api/v1/matches/', response_model=schemas.Match, tags=['matches'])
def create_match(game_id: int, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_game = crud.get_game_by_id(db, game_id)
    
    if not db_game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Game not found')
    
    match = schemas.MatchCreate(player1=current_user.id, game=game_id)

    return crud.create_match(db, match)


@router.put('/api/v1/matches/{match_id}', response_model=schemas.Match, tags=['matches'])
def update_match(match_id: int, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_match = crud.get_match_by_id(db, match_id)

    if not db_match:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Match not found')

    if db_match.player2:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='player2 already exists')

    if db_match.player1 == current_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='player1 and player2 cannot be the same player')

    return crud.update_match(db, match_id, current_user)
