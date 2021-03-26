from fastapi import FastAPI

import socketio

app = FastAPI()

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins=['http://localhost:8080'])
socket_app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, environ):
    print('connect ', sid)
    await sio.emit('hello', 'Can you hear me?')

@sio.event
async def ack(sid, data):
    print('ack ', sid, data)

app.mount('/', socket_app)
