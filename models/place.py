#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            nullable=False),
    Column(
            'amenity_id',
            String(60),
            ForeignKey('amenities.id'),
            nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship(
                                'Review',
                                cascade='all, delete',
                                backref='place')
        amenities = relationship(
                                'Amenity',
                                secondary=place_amenity,
                                viewonly=False,
                                back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """Getter attribute reviews that returns the list of Review"""
            from models.review import Review
            from models.__init__ import storage
            list_reviews = []
            reviews = storage.all(Review)
            for review in reviews.values():
                if review.place_id == self.id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            """Getter attribute amenities that returns the list of Amenity"""
            from models.amenity import Amenity
            from models.__init__ import storage
            all_amenities = storage.all(Amenity)
            list_return = []
            for key, value in all_amenities.items():
                if self.id == value.place_id:
                    list_return.append(value)
            return list_return