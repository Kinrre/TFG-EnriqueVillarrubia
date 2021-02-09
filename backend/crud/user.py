from sqlalchemy.orm import Session

from backend import models, schemas

import bcrypt

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
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(user.password.encode(), salt)
    
    db_user = models.User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_password(db: Session, new_password: str, user: schemas.UserCreate):
    """Update the password of a user to the database."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(new_password.encode(), salt)
    
    db_user = get_user_by_username(db, user.username)
    db_user.password = hashed_password
    db.commit()
    db.refresh(db_user)

    return db_user
