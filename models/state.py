#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, relationship

class State(BaseModel, Base):
    """ State class """
    name = ""
    places = relationship("Child")
