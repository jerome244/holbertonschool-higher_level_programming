#!/usr/bin/python3
"""
model_city.py: Defines the City class for ORM mapping to the 'cities' table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import State

Base = declarative_base()


class City(Base):

    """
    City ORM class mapped to the 'cities' table.

    Attributes:
        id (int): Auto-generated primary key, non-nullable.
        name (str): City name, max length 128, non-nullable.
        state_id (int): Foreign key to states.id, non-nullable.

    Relationships:
        state (State): The State object this city belongs to.
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", back_populates="cities")


State.cities = relationship("City", order_by=City.id, back_populates="state")
