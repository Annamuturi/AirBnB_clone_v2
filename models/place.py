#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models


if getenv("HBNB_TYPE_STORAGE") == 'db':
    place_amenity = Table(
            "place_amenity", Base.metadata,
            Column("place_id", String(60), ForeignKey("places.id"),
                   primary_key=True, nullable=False),
            Column("amenity_id", String(60), ForeignKey("amenities.id"),
                   primary_key=True, nullable=False)
            )


class Place(BaseModel, Base):
    """Defines a place"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", cascade="all, delete-orphan",
                               backref="place")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Returns list of reviews linked to the Place instance"""
            all_reviews = models.storage.all("Review").values()
            place_reviews = [review for review in all_reviews
                             if review.place_id == self.id]
            return place_reviews

        @property
        def amenities(self):
            """Returns list of amenities linked to the Place instance"""
            all_amenities = models.storage.all("Amenity").values()
            plc_amenities = [amenity for amenity in all_amenities
                             if amenity.place_id == self.id]
            return plc_amenities

        @amenities.setter
        def amenities(self, obj):
            """Appends object's id to amenity_ids if obj is an Amenity"""
            if isinstance(obj, models.amenity.Amenity):
                self.amenity_ids.append(obj.id)
