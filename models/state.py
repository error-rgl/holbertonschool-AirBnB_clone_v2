#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":

        cities = relationship("City", cascade="all, delete", backref="states")
    else:
        name = ""

        @property
        def cities(self):
            """returns the list of City instances with state_id"""
            cities_list = []
            _cities = models.storage.all(City)
            for _city in _cities.values():
                if self.id == _city.state_id:
                    cities_list.append(_city)
            return cities_list
