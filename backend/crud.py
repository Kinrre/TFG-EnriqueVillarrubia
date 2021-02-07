from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id: int):
    """Get a user from the database by his id."""
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    """Get a user from the database by his username."""
    return db.query(models.User).filter(models.User.username == username).first()   


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Get multiple users from the database given a offset and a limit."""
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    """Create a user to the database given a UserCreate schema."""
    hashed_password = user.password
    db_user = models.User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


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
