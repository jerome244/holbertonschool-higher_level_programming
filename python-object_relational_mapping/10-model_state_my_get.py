#!/usr/bin/python3
"""10-model_state_my_get.py: Prints the State id of the State object with the given name from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    user, password, database, name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{database}",
        pool_pre_ping=True
    )
    # Ensure table exists
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Safe query to find the state by name
    state = session.query(State).filter(State.name == name).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
