#!/usr/bin/python3
"""
model_state module: contains the State class and Base declarative base for ORM mapping.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class mapped to the 'states' table.

    Attributes:
        id (int): Primary key, auto-generated, non-nullable.
        name (str): State name, max length 128, non-nullable.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
