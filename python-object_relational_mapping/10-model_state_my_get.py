#!/usr/bin/python3
"""Prints the State id with the given name from hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    user, pwd, db, name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost/{db}", pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == name).first()
    print(state.id if state else "Not found")

    session.close()
