#!/usr/bin/python3
"""a script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import re


if __name__ == '__main__':

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]

    """create an engine"""
    db_url = f'mysql+mysqldb://{USER}:{PASS}@localhost:3306/{DB}'
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    """create a configured 'Session' class"""
    Session = sessionmaker(bind=engine)

    """create a Session"""
    session = Session()

    pattern = r'^.*a.*$'
    _all = session.query(State).all()
    state_list = []
    for state in _all:
        if (re.search(pattern, state.name)):
            state_list.append(state.name)
    AllStates = session.query(State) \
        .filter(State.name.in_(state_list)) \
        .order_by(State.id) \
        .all()

    for state in AllStates:
        print(f'{state.id}: {state.name}')

    session.close()
