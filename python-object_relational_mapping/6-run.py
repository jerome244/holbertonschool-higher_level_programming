#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from model_state import Base

engine = create_engine(
    f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
    pool_pre_ping=True,
)
Base.metadata.create_all(engine)
