import os
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
#sys.path.insert(0, PROJECT_ROOT) # no import from local dir

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
 
Base = declarative_base()



class Cases(Base):
    __tablename__ = 'cases'

    state          = Column(String(25), primary_key = True)
    totalcases        = Column(Integer)
    newcases        = Column(Integer)
    totaldeath        = Column(Integer)
    newdeath        = Column(Integer)
    totalrecovered        = Column(Integer)
    serious        = Column(Integer)
	
    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'state'         : self.state,
           'cases'           : self.totalcases,
           'death'      : self.totaldeath,
       }


class Admins(Base):
    __tablename__ = 'admins'

    username          = Column(String(25), primary_key = True)
    password        = Column(String(25), nullable = False)
    totalviews =  Column(Integer)
    
	
   
    



engine = create_engine('postgresql://database:<123>@localhost/database')

Base.metadata.create_all(engine)

