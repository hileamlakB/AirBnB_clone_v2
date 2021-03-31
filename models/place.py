#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import Review, Place, Amenity
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, relationship

metadata = Base.metadata
place_amenity = Table('place_aminity', metadata, Column('place_id', String(60, primarykey=True, ForiegnKey("places.id"))), Column('amenity_id', String(60), ForiegnKey("amenities.id")))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey("cities.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)u
    number_rooms = Column(Integer, nullable=False, default=1)
    number_bathrooms = Column(Integer, nullable=False, default=1)
    max_guest = Column(Integer, nullable=False, default=1)
    price_by_night = Column(Integer, nullable=False, default=1)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review')
    amenity_ids = []
    amenities = relationship("Amenity", secondary = place_amenity, backref="places", viewonly=False)

    # Add setter and getters for the filestorage
