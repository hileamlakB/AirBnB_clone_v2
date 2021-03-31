#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="save-update, delete")
