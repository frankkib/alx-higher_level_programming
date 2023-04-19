#!/usr/bin/python3

"""Module that contains class defination"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Create an instance of the declarative base class
Base = declarative_base()


class State(Base):

    """Class state defination"""

    __tablename__ = 'states'

    id = Column(
            Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    
    def __repr__(self):
        """returns a string"""
        return f"State(id={self.id}, name='{self.name})'"
