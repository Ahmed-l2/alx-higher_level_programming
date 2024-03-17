#!/usr/bin/python3

"""
This script prints the State object id
with the name passed as argument
from the database `hbtn_0e_6_usa`.
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine_url = f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"
    engine = create_engine(engine_url)
    session = sessionmaker(bind=engine)()

    instance = session.query(State).filter(State.name == argv[4]).first()

    if instance is None:
        print('Not found')
    else:
        print('{0}'.format(instance.id))
