from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from multiprocessing import Process

from backend_players.players.main import train
from backend_players.core.config import GAME_URL

import requests

router = APIRouter()

@router.post('/api/v1/train/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['train'])
async def train_game(id: int):
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

    proc =  Process(target=train, args=(game_json, model)) # Create the process of training
    proc.start() # Start the process

    return {'detail': 'Player training request sent, check the id for the status', 'id': game_json['id']}
