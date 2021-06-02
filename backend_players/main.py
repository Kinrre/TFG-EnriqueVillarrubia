from fastapi import FastAPI

from backend_players.api.v1 import train

app = FastAPI(
    title='Backend Players API',
    description='API definition for the generation of players.'
)

app.include_router(train.router)
