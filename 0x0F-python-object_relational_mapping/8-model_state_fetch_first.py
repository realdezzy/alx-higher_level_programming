#!/usr/bin/python3
""" Fetch first state """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

from sys import argv


def fetch_first(engine):
    """Fetch state and print nicely formated output """
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()

    print("{:d}: {}".format(state.id, state.name))


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
            '.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    fetch_first(engine)
