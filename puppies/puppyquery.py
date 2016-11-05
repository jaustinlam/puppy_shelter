import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import Base, Puppy, Shelter
engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
sess = DBSession()


def allPuppies():
    '''Query all puppies and return results in ascending order

    '''
    print "1. Query all of the puppies and return the results in ascending alphabetical order"
    for x in sess.query(Puppy).order_by(Puppy.name.asc()):
        print x.name


def youngPups():
    '''Queries all puppies < 6 months sorted by youngest

    '''
    print "2. Query all of the puppies that are less than 6 months old organized by the youngest first"
    todaySixMonths = datetime.date.today() - datetime.timedelta(180)

    for x in sess.query(Puppy).filter(
        Puppy.dateOfBirth > todaySixMonths).order_by(
        Puppy.dateOfBirth ).all():
        print x.name, x.dateOfBirth
        print '\n'


def weightPups():
    '''Queries all puppies by ascending weight.

    '''
    print "3. Query all puppies by ascending weight"

    for x in sess.query(Puppy).order_by(Puppy.weight.asc()):
        print x.name, x.weight
        print '\n'



def pupsByShelter():
    '''Queries all puppies grouped by shelter.

    '''
    print "4. Query all puppies grouped by the shelter in which they are staying"

    for x in sess.query(Puppy).order_by(Puppy.shelter_id.asc()).all():
        print x.name, x.shelter_id
        print '\n'



print allPuppies()
print youngPups()
print weightPups()
print pupsByShelter()


