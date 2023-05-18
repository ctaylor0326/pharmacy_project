from sqlalchemy import (ForeignKey, Column, Integer, String, Float, create_engine)
from sqlalchemy.orm import Session, declarative_base

# engine = create_engine('sqlite:///pharmacy.db')

Base = declarative_base()

class Medication(Base):
   

    __tablename__ = 'medications'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    dosage = Column(String())
    quantity = Column(Integer())
    price = Column(Float())


    def __repr__(self):
        return f'Medication:{self.name} Quantity:{self.quantity} Price:{self.price}'
        # return f'Medication:' + \
        #     f'name={self.name}, ' + \
        #     f'price={self.price})'
    

class Patient(Base):

    __tablename__ = 'patients'

    id = Column(Integer(), primary_key=True)
    last_name = Column(String())
    first_name = Column(String())
    address = Column(String())
    
    def __repr__(self):
        return f'{self.first_name} {self.last_name})'

class Prescription(Base):
    __tablename__ = 'prescriptions'

    id = Column(Integer(), primary_key=True)
    patient_id = Column(Integer(), ForeignKey('patients.id'))
    prescription_id = Column(Integer(), ForeignKey('prescriptions.id'))


class ShoppingCart(Base):
    __tablename__ = 'shopping_carts'

    id = Column(Integer(), primary_key=True)


if __name__ == '__main__':
    engine = create_engine('sqlite:///pharmacy.db')
    
    Base.metadata.create_all(engine)



   