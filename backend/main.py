from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import Base, engine
from backend.api.v1 import auth, games, matches, users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Backend API',
    description='API definition for the backend of users, games and matches.'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8080'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(auth.router)
app.include_router(games.router)
app.include_router(matches.router)
app.include_router(users.router)

""" SOCKET.IO
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins=["http://localhost:8080"])
socket_app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, environ):
    print('connect ', sid)
    await sio.emit("hello", "Can you hear me?")

@sio.event
async def ack(sid, data):
    print('ack ', sid, data)

app.mount('/', socket_app)
"""
