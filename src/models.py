import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    date = Column(Date, index=True)

    def to_dict(self):
        return {}
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(String(250), primary_key=True)
    user = Column(Integer, nullable=True)
    planet_origin = Column(Integer, ForeignKey('planet.id'))
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)

    def to_dict(self):
        return {}
    
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(String(250), primary_key=True)
    user = Column(Integer, nullable=True)
    brand = Column(String(250), nullable=False)
    spaces = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)


    def to_dict(self):
        return {}
    
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(String(250), primary_key=True)
    user = Column(Integer, nullable=True)
    wheather = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    rotation_period = Column()

    def to_dict(self):
        return {}
    
class Movies(Base):
    __tablename__ = 'movies'
    id = Column(String(250), primary_key=True)
    name = Column(String(250), nullable=False)
    year = Column(Date, index=True)
    director = Column(String(250), nullable=False)
    duration = Column(String(250), nullable=False)

    def to_dict(self):
        return {}
    
class Director(Base):
    __tablename__ = 'director'
    id = Column(String(250), primary_key=True)
    age = Column(Integer, nullable=False)
    lastname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)

class MyFavorites(Base):
    __tablename__ = 'My Favorties'
    id = Column(Integer, primary_key=True)
    user = Column(String(250), ForeignKey('user.id'))
    planet = Column(Integer, ForeignKey('planet.id'))
    director = Column(Integer, ForeignKey('director.id'))
    movie = Column(Integer, ForeignKey('movies.id'))
    vehicle = Column(Integer, ForeignKey('vehicle.id'))
    character = Column(Integer, ForeignKey('character.id'))
    def to_dict(self):
        return {}
    
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
