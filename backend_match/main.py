from fastapi import FastAPI

import socketio

app = FastAPI()

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins=['http://localhost:8080'])
socket_app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, environ):
    print('connect ', sid)


@sio.event
async def join(sid, roomCode):
    # Join the player into a room with name 'roomCode'
    # TODO: Check maximum size!
    print('enter room', sid, roomCode, flush=True)
    sio.enter_room(sid, roomCode)


@sio.event
async def room_completed(sid, data):
    # Emit in the room that second player has joined
    await sio.emit('roomCompleted', data['playerName'], room=data['roomCode'])


@sio.event
async def move(sid, data):
    # Emit in the room a movement
    await sio.emit('move', data, room=data['roomCode'])


@sio.event
async def end_game(sid, data):
    # Emit in the room the end of a game
    await sio.emit('endGame', data, room=data['roomCode'])


app.mount('/', socket_app)
