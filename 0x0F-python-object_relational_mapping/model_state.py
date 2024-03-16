#!/usr/bin/python3


from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    __tablename__ = "states"

    state_id = Column("id", Integer, primary_key=True, autoincrement=True,
                nullable=False)

    state_class = Column("class", String(128), nullable=False)
