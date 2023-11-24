#!/usr/bin/python3
"""
a script that lists all City objects from the
database hbtn_0e_101_usa

"""

from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

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

    Allstates = session.query(State)
    for state in Allstates:
        for city in state.cities:
            print(f'{city.id}: {city.name} -> {state.name}')

    session.close()
