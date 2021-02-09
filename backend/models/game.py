from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.database import Base

class Game(Base):
    """Game database model."""
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    model = Column(String, unique=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='games')
