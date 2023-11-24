#!/usr/bin/python3
"""
a script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa

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

    # _ = State(name="California", cities=[City(name="San Francisco")])

    state = State(name='California')
    session.add(state)
    session.commit()

    city = City(name='San Francisco', state_id=state.id)
    session.add(city)
    session.commit()

    session.close()
