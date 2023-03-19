#!/usr/bin/python3
""" Delete rows """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

from sys import argv


def delete_row(engine):
    """Delete rows matching a pattern"""

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
            '.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    delete_row(engine)
