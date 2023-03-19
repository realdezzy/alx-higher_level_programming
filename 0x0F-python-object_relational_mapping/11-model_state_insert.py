#!/usr/bin/python3
""" Fetch all States """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

from sys import argv


def add_state(engine):

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name=argv[4])

    session.add(new_state)
    session.commit()
    print("{:d}".format(new_state.id))


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
            '.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    add_state(engine)
