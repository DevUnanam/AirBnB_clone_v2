#!/usr/bin/python3
"""Here, the amentiy class is defined"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This represents the class for Amenity
    Attributes:
        name: The amenity name
        place_amenities: Place-Amenity Relationship
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
