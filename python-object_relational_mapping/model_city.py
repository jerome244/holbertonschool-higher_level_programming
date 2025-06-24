#!/usr/bin/python3
"""
model_city.py: contains the class definition of a City for SQLAlchemy ORM, linking to the 'cities' table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State

class City(Base):
    """
    City class mapped to the 'cities' table.

    Attributes:
        id (int): Primary key, auto-generated, non-nullable.
        name (str): City name, max length 128, non-nullable.
        state_id (int): Foreign key to states.id, non-nullable.
    Relationship:
        state (State): The associated State object.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('State', back_populates='cities')

# Establish back-population on State
State.cities = relationship('City', order_by=City.id, back_populates='state')
