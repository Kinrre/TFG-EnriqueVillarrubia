from sqlalchemy import and_
from sqlalchemy.orm import Session

from backend import models, schemas

def create_user_game(db: Session, game: schemas.GameCreate, user_id: int):
    """Create a game to the database given a GameCreate schema and the owner."""
    db_game = models.Game(**game.dict(), owner_id=user_id)
    
    db.add(db_game)
    db.commit()
    db.refresh(db_game)

    return db_game


def delete_game(db: Session, name: str, current_user: schemas.User):
    """Delete a game from the database given his name and the owner."""
    db_game = get_game_by_name(db, name, current_user)

    db.delete(db_game)
    db.commit()


def get_games(db: Session, skip: int = 0, limit: int = 100):
    """Get games given an offset and a limit."""
    return db.query(models.Game).offset(skip).limit(limit).all()


def get_games_current_user(db: Session, current_user: schemas.User, skip: int = 0, limit: int = 100):
    """Get games given an offset and a limit for a specific user."""
    db_games = db.query(models.Game).filter(
        models.Game.owner_id == current_user.id
    ).offset(skip).limit(limit).all()
    return db_games


def get_game_by_id(db: Session, game_id: int):
    """Get a game from the database by his id."""
    db_game = db.query(models.Game).filter(
        models.Game.id == game_id
    ).first()
    return db_game


def get_game_by_name(db: Session, name: str, current_user: schemas.User):
    """Get a game from the database by his name."""
    db_game = db.query(models.Game).filter(
        and_(models.Game.name == name, models.Game.owner_id == current_user.id)
    ).first()
    return db_game


def update_current_user_game(db: Session, name: str, game_update: schemas.GameUpdate, current_user: schemas.UserCreate):
    """Update the game of a user to the database."""
    db_game = get_game_by_name(db, name, current_user)

    if game_update.new_name != None:
        db_game.name = game_update.new_name

    if game_update.trained != None:
        db_game.trained = game_update.trained

    db.commit()
    db.refresh(db_game)

    return db_game
