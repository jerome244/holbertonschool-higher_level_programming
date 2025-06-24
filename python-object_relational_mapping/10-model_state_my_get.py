#!/usr/bin/ python3
"""Prints the State id matching the name passed as argument."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def main():
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    session = Session(engine)

    result = session.query(State).filter(State.name == sys.argv[4]).one_or_none()
    print(result.id if result else "Not found")
    session.close()


if __name__ == "__main__":
    main()
