#!/usr/bin/python3

"""
This script adds the State object
`Louisiana` to the database `hbtn_0e_6_usa`.
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    new_state_id = session.query(State).filter(State.name == "Louisiana").first()
    print('{0}'.format(new_state_id))
