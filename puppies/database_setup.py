import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

class Shelter(Base):
    ''' Class to represent the Shelters information

        Args:
            Base which is the declarative_base

    '''

    __tablename__ = 'shelter'

    name = Column(
        String(80), nullable = False)

    address = Column(
        String(250), nullable = False)

    city = Column(
        String(80), nullable = False)

    state = Column(
        String(80), nullable = False)

    zipcode = Column(
        String(10), nullable = False)

    website = Column(
        String(80), nullable = False)

    id = Column(
        Integer, primary_key = True)

class Puppy(Base):
    ''' Class to represent individual puppies

        Args:
            Base which is the declarative_base

    '''
    __tablename__ = 'puppy'

    name = Column(
        String(80), nullable = False)

    id = Column(
        Integer, primary_key = True)

    dateOfBirth = Column(
        Date, nullable = False)

    gender = Column(
        String(6), nullable = False)

    weight = Column(
        Float, nullable = False)


    shelter_id = Column(
        Integer, ForeignKey('shelter.id'))

    shelter = relationship(Shelter)


engine = create_engine(
    'sqlite:///puppies.db')
Base.metadata.create_all(engine)

