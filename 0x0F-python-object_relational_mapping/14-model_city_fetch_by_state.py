#!/usr/bin/python3
"""a script that prints all City objects
from the database hbtn_0e_14_usa"""

from model_state import State, Base
from model_city import City
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

    for c, s in session.query(City, State) \
            .filter(City.state_id == State.id) \
            .all():
        print(f'{s.name}: ({c.id}) {c.name}')

    session.close()
