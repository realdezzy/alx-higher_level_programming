#!/usr/bin/python3
""" Fetch state passed as user argument"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

from sys import argv


def fetch_from_term(engine):
    """Fetch state and print nicely formated output """
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        state = session.query(State).filter(State.name == argv[4]).one()
        print("{:d}".format(state.id))
    except Exception as e:
        print("Not Found")


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
            '.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    fetch_from_term(engine)
