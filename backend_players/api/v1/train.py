from backend.schemas import game
from fastapi import APIRouter, BackgroundTasks, status
from fastapi.exceptions import HTTPException

from backend_players.players.main import train
from backend_players.core.config import GAME_URL

import requests

router = APIRouter()

@router.post('/api/v1/train/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['train'])
async def train_game(id: int, background_tasks: BackgroundTasks):
    game_response = requests.get(GAME_URL + str(id)) # Get the game configuration

    if game_response.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=game_response.json()['detail'])

    game_json = game_response.json()

    if game_json['is_trained']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Game already trained')

    if game_json['is_training']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Game already training')

    model = 'backend_players/players/models/' + game_json['model'] # Obtain the model of the game

    background_tasks.add_task(train, game_json, model)

    return {'detail': 'Player training request sent'}
