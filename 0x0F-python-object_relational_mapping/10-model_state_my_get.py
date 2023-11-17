#!/usr/bin/python3
"""a script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]
    state_arg = sys.argv[4]

    """create an engine"""
    db_url = f'mysql+mysqldb://{USER}:{PASS}@localhost:3306/{DB}'
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    """create a configured 'Session' class"""
    Session = sessionmaker(bind=engine)

    """create a Session"""
    session = Session()

    try:
        state = session.query(State).filter(State.name == state_arg)
        print(f'{state[0].id}')
    except IndexError:
        print('Not found')

    finally:
        session.close()
