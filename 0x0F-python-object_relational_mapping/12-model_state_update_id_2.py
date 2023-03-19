#!/usr/bin/python3
""" Update Column Script """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

from sys import argv


def update_state(engine):
    """Update Script"""

    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        to_up = session.query(State).filter(State.id == 2).one()
        to_up.name = "New Mexico"
        session.commit()
    except Exception as e:
        pass


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
            '.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    update_state(engine)
