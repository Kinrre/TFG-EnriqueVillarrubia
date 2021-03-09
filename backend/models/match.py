from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.schema import UniqueConstraint

from backend.database import Base

import secrets

class Match(Base):
    """Match database model."""
    __tablename__ = 'matches'
    __table_args__ = (UniqueConstraint('room_code'),)

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey('games.id', ondelete=None))
    player1_id = Column(Integer, ForeignKey('users.id', ondelete=None))
    player2_id = Column(Integer, ForeignKey('users.id', ondelete=None))
    room_code = Column(String, default=secrets.token_urlsafe(4))
    winner = Column(Integer, ForeignKey('users.id', ondelete=None), default=None)

    game = relationship('Game')
    player1 = relationship('User', foreign_keys=[player1_id])
    player2 = relationship('User', foreign_keys=[player2_id])
