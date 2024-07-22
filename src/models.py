import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorite(Base):
    __tablename__ = "favorite"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    character_id = Column(Integer)
    planet_id = Column(Integer)
    starship_id = Column(Integer)

   
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates = "favorites")

    
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship("Character", back_populates = "favorites")

   
    planet_id = Column(Integer, ForeignKey("planet.id"))
    planet = relationship("Planet", back_populates = "favorites")

    
    starship_id = Column(Integer, ForeignKey("starships.id"))
    starship = relationship("Starship", back_populates = "favorites")


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)
    password = Column(String(250))

    
    favorites = relationship("Favorite", back_populates = "user")


class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    race = Column(String(250))
    height = Column(String(250))
    eye_color = Column(String(250))
    side = Column (String(250))

   
    favorites = relationship("Favorite", back_populates = "character")

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    capital = Column(String(250))

   
    favorites = relationship("Favorite", back_populates = "planet")

class Starships(Base):
    __tablename__ = "starships"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    capacity = Column(String(250))
    max_speed = Column(String(250))

    
    favorites = relationship("Favorite", back_populates = "starships")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')