#!/usr/bin/python3
"""
9-model_state_filter_a.py
Lists all State objects containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    if len(sys.argv) != 4:
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@"
        f"localhost/{database}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for states containing the letter 'a'
    states_with_a = (
        session.query(State)
        .filter(State.name.like("%a%"))
        .order_by(State.id)
    )
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    main()
