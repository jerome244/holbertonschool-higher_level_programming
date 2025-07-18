#!/usr/bin/python3
"""
14-model_city_fetch_by_state.py
Print all City objects from the database hbtn_0e_14_usa.

Usage:
  ./14-model_city_fetch_by_state.py \
  <mysql_username> <mysql_password> <database_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    if len(sys.argv) != 4:
        sys.exit(1)

    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@"
        f"localhost/{database}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch and print cities in order
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(
            f"{city.state.name}: ({city.id}) {city.name}"
        )

    session.close()


if __name__ == "__main__":
    main()
