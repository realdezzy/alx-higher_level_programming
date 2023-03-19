#!/usr/bin/python3
""" Fetch all States """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City
from sys import argv


def fetch_all_cities(engine):

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State, City).filter(City.state_id == State.id).all()

    for i in range(len(states)):
        print("{}: ({:d}) {}".format(states[i][0].name,
                                     states[i][1].id, states[i][1].name))


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
            '.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    fetch_all(engine)
