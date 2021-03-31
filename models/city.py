#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, relationship

class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = Column(Integer, ForeignKey("states.id"))
    name = ""
