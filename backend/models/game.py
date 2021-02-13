from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import UniqueConstraint

from backend.database import Base

import uuid

class Game(Base):
    """Game database model."""
    __tablename__ = 'games'
    __table_args__ = (UniqueConstraint('name', 'owner_id'),)

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    model = Column(String, unique=True, index=True, default=str(uuid.uuid4()))
    trained = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))

    owner = relationship('User', back_populates='games')
