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


# 14-model_city_fetch_by_state.py
"""
14-model_city_fetch_by_state.py: Prints all City objects from the database hbtn_0e_14_usa.
Usage: ./14-model_city_fetch_by_state.py <mysql_username> <mysql_password> <database_name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(1)

    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{database}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities ordered by id, including their state relationship
    for city in session.query(City).order_by(City.id).all():
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()
