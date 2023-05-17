from sqlalchemy import (ForeignKey, Column, Integer, String, Float)
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:///pharmacy.db')

Base = declarative_base()

class Prescription(Base):
   

    __tablename__ = 'prescriptions'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    dosage = Column(String())
    quantity = Column(Integer())
    price = Column(Float())


    def __repr__(self):
        return f'Prescription(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'price={self.price})'
    

class Patient(Base):

    __tablename__ = 'patients'

    id = Column(Integer(), primary_key=True)
    last_name = Column(String())
    first_name = Column(String())
    address = Column(String())
    
    def __repr__(self):
        return f'{self.first_name} {self.last_name})'

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer(), primary_key=True)
    patient_id = Column(Integer(), ForeignKey('patients.id'))
    prescription_id = Column(Integer(), ForeignKey('prescriptions.id'))


class ShoppingCart(Base):
    __tablename__ = 'shopping_carts'

    id = Column(Integer(), primary_key=True)