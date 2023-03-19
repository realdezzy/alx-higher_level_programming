#!/usr/bin/python3
""" Fetch all States """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

from sys import argv


def fetch_all(engine):

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()

    for i in range(len(states)):
        print("{:d}: {}".format(states[i].id, states[i].name))


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
            '.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    fetch_all(engine)
