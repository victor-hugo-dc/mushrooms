from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import pandas as pd

Base = declarative_base()

class Mushrooms(Base):
    __tablename__ = 'mushrooms'
    __table_args__ = {'sqlite_autoincrement': True}
    order = Column(String(100))
    family = Column(String(100))
    genus = Column(String(100))
    species = Column(String(100))
    infraspecificEpithet = Column(String(100))
    scientificName = Column(String(100))
    verbatimScientificName = Column(String(100))
    countryCode = Column(String(100))
    locality = Column(String(100))
    uniqueID = Column(Integer, primary_key = True, nullable = False)

class Locations(Base):
    __tablename__ = 'locations'
    __table_args__ = {'sqlite_autoincrement': True}
    uniqueID = Column(Integer, primary_key = True, nullable = False)
    decimalLatitude = Column(Float)
    decimalLongitude = Column(Float)

engine = create_engine('sqlite:///gbif.db')
Base.metadata.create_all(engine)

gbif: pd.DataFrame = pd.read_csv("./data/cleaned/gbif.csv", index_col = 'Unnamed: 0')
gbif.to_sql(con = engine, index_label = 'ID', name = Mushrooms.__tablename__, if_exists = 'replace')

engine = create_engine('sqlite:///locations.db')
Base.metadata.create_all(engine)

locations: pd.DataFrame = pd.read_csv("./data/cleaned/locations.csv", index_col = 'Unnamed: 0')
locations.to_sql(con = engine, index_label = 'ID', name = Locations.__tablename__, if_exists = 'replace')