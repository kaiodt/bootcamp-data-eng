from db import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func


class Pokemon(Base):
    __tablename__ = 'pokemons'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    types = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
