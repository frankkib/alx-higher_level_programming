#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # create the connection to the database
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, db_name), pool_pre_ping=True)

    # create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the database and display the result
    res = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in res:
        print("{}: {}".format(state.id, state.name))
