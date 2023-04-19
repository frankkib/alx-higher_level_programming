#!/usr/bin/python3
"""linking a class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """class defination"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=True,
            autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", backref="cities")
