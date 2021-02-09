from sqlalchemy.orm import Session

from backend import models, schemas

def get_game(db: Session, game_id: int):
    """Get a game from the database by his id."""
    return db.query(models.Game).filter(models.Game.id == game_id).first()


def get_game_by_name(db: Session, name: str):
    """Get a game from the database by his name."""
    return db.query(models.Game).filter(models.Game.name == name).first()   


def get_games(db: Session, skip: int = 0, limit: int = 100):
    """Get multiple games within a given offset and limit."""
    return db.query(models.Game).offset(skip).limit(limit).all()


def create_user_game(db: Session, game: schemas.GameCreate, user_id: int):
    """Create a game to the database given a GameCreate schema and the owner."""
    db_game = models.Game(**game.dict(), owner_id=user_id)
    
    db.add(db_game)
    db.commit()
    db.refresh(db_game)

    return db_game
