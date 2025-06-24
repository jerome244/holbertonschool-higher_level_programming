#!/usr/bin/python3
"""
Module model_state
Defines Base and State class linked to the 'states' table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Declarative base instance
Base = declarative_base()


class State(Base):
    """
    State class mapped to 'states' table:
    - id: auto-generated primary key
    - name: non-nullable string up to 128 chars
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
