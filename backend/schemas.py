from typing import List
from pydantic import BaseModel

class GameBase(BaseModel):
    """Base game schema."""
    name: str


class GameCreate(GameBase):
    """Create game schema."""
    pass


class Game(GameBase):
    """Complete game schema without id."""
    model: str
    owner_id: int

    class Config:
        orm_mode = True
        

class UserBase(BaseModel):
    """Base user schema."""
    username: str


class UserCreate(UserBase):
    """Create user schema."""
    password: str


class User(UserBase):
    """Complete user schema without id."""
    is_active: bool
    games: List[Game] = []

    class Config:
        orm_mode = True
