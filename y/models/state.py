#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """This is a class of State

    Attributes:
        __tablename__: name of mysql table

        name: State name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

