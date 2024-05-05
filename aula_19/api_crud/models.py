from database import Base
from sqlalchemy import Boolean, Column, Float, Integer, String


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    price = Column(Float, nullable=False)
    is_offer = Column(Boolean, default=False)
