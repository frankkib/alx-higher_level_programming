#!/usr/bin/python3
"""
Lists all State objects from the database
"""
import sys
import sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    #connection
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
            '.format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    #session set up
    session = sessionmaker(bind=engine)
    session = session()
    #query
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
