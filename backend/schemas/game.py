from typing import Optional
from pydantic import BaseModel

class GameBase(BaseModel):
    """Base game schema."""
    name: str
    board_size: int
    fen: str


class GameCreate(GameBase):
    """Create game schema."""
    pass


class GameUpdate(BaseModel):
    """Update game schema."""
    new_name: Optional[str] = None
    trained: Optional[bool] = None


class Game(GameBase):
    """Complete game schema without id."""
    id: int
    model: str
    owner_id: int
    trained: bool = False

    class Config:
        orm_mode = True
