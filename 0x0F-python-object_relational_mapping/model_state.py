#!/usr/bin/python3
"""
Defines a SQLAlchemy ORM model for representing states
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                      nullable=False)

    name = Column(String(128), nullable=False)
