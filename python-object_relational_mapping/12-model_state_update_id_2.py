#!/usr/bin/python3
"""12-model_state_update_id_2.py: Changes the name of the State object with id=2 to New Mexico in the database hbtn_0e_6_usa."""

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
    # Ensure table is available
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the state with id=2
    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
