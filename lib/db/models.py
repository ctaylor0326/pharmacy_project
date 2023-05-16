from sqlalchemy import (PrimaryKeyConstraint, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:///pharmacy.db')

Base = declarative_base()

class Prescription(Base):

    __tablename__ = 'prescription'

    __table_args__ = (PrimaryKeyConstraint('id'), )

    id = Column(Integer())
    name = Column(String())
    dosage = Column(String())
    