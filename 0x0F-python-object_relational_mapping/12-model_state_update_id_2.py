#!/usr/bin/python3
"""a script that changes the name of a State object
from the database hbtn_0e_6_usa"""

from model_state import State, Base
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

    try:
        NAME = 'New Mexico'
        state = session.query(State).filter(State.id == 2)
        state[0].name = NAME
        session.commit()
    except IndexError as e:
        print(e)
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()
