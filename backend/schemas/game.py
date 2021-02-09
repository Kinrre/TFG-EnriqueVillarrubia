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
