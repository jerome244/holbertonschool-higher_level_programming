#!/usr/bin/python3
"""Prints the first State object from hbtn_0e_6_usa."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    user, pwd, db = argv[1], argv[2], argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost/{db}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).order_by(State.id).first()
    print(f"{first.id}: {first.name}" if first else "Nothing")
    session.close()
