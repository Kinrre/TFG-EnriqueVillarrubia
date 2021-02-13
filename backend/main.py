from fastapi import FastAPI

from backend.database import Base, engine
from backend.api.v1 import auth, users, games

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Backend API',
    description='API definition for the backend of users and games.'
)
app.include_router(auth.router)
app.include_router(games.router)
app.include_router(users.router)
