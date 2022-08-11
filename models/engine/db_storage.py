#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity


"""Environmental Variables"""
user = os.getenv("HBNB_MYSQL_USER")
pasw = os.getenv("HBNB_MYSQL_PWD")
host = os.getenv("HBNB_MYSQL_HOST")
db = os.getenv("HBNB_MYSQL_DB")
env = os.getenv("HBNB_ENV")
engine_txt = 'mysql+mysqldb://' + user + ':' + pasw + '@' + host + '/' + db


class DBStorage():
    """Constructor of the class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(engine_txt, pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns the list of objects of one type of class or all"""
        objs = []
        dic = {}
        if cls is None:
            classes = [Base, State, City, Place, Review, User, Amenity]
            for cls in classes:
                objs.extend(self.__session.query(cls).all())
        else:
            objs.extend(self.__session.query(cls).all())

        for obj in objs:
            dic[obj.__class__.__name__ + '.' + obj.id] = obj
        return dic

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creating tables"""
        Base.metadata.create_all(self.__engine)
        """Creating a configurable Session factory"""
        fact_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        """Creating a scoped_session is constructed by calling it,
        passing it a factory which can create new Session objects."""
        session = scoped_session(fact_session)
        """Creating a session"""
        self.__session = session()

    def close(self):
        """Close de current session"""
        self.__session.close()

