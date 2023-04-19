#!/usr/bin/python3

"""module that contains class defination"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the declarative base class
Base = declarative_base()


class State(Base):

    """class state defination"""

    __table__ = 'states'

    id = Column(
            Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    
    def __repr__(self):
        return f"State(id={self.id}, name='{self.anme}'"
