#!/usr/bin/python3
"""13-model_state_delete_a.py: Deletes all State objects with names containing the letter 'a' from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{database}", pool_pre_ping=True
    )
    # Ensure table exists
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete states with names containing 'a'
    session.query(State).filter(State.name.like("%a%")).delete(
        synchronize_session="fetch"
    )
    session.commit()

    session.close()
