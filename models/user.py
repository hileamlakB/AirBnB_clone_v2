#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models import Place, Review
from sqlalchemy import Column, Integer, String, ForeignKey, Float, relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    places = relationship("Place")
    reviews = relationship("Review")
