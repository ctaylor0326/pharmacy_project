from sqlalchemy import ForeignKey, Column, Integer, String, Numeric, Float, create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, column_property
from sqlalchemy.ext.associationproxy import association_proxy
# from sqlalchemy.ext.hybrid import hybrid_property

engine = create_engine('sqlite:///pharmacy.db')

Base = declarative_base()


class Medication(Base):
    __tablename__ = 'medications'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    type = Column(String())
    dosage = Column(String())
    quantity = Column(Integer())
    price = Column(Float(precision=8, asdecimal=True, decimal_return_scale=2))
    # Formatted price property
    # @hybrid_property
    def formatted_price(self):
        return "${:,.2f}".format(self.price)
    # # Column property for formatted price
    # formatted_price_col = column_property(formatted_price)
    # access the formatted price as 
    #   medication_instance.formatted_price 
    prescriptions = relationship('Prescription', back_populates='medication')
    patients = association_proxy(
        'prescriptions', 'patient', creator=lambda us: Prescription(patient=us))

    def __repr__(self):
        return f'Medication:{self.name} Quantity:{self.quantity} Price:{self.formatted_price}'
        # return f'Medication:' + \
        #     f'name={self.name}, ' + \
        #     f'price={self.price})'


class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer(), primary_key=True)
    last_name = Column(String())
    first_name = Column(String())
    address = Column(String())
    username = Column(String())
    password = Column(String())
    prescriptions = relationship('Prescription', back_populates='patient')
    medications = association_proxy(
        'prescriptions', 'medication', creator=lambda us: Prescription(medication=us))

    def __repr__(self):
        return f'{self.first_name} {self.last_name})'


class ShoppingCart(Base):
    __tablename__ = 'shopping_carts'
    id = Column(Integer(), primary_key=True)
    script_id = Column(Integer(), ForeignKey('medications.id'))
    # otc_id = Column(Integer(), ForeignKey('otc.id'))
    name = Column(String())
    price = Column(Float(precision=8, asdecimal=True, decimal_return_scale=2))
    
    def formatted_price(self):
        return "${:,.2f}".format(self.price)
    
    def __repr__(self):
        return f'Medication:{self.name} Quantity:{self.quantity} Price:{self.formatted_price}'

class Prescription(Base):
    __tablename__ = 'prescriptions'
    id = Column(Integer(), primary_key=True)
    patient_id = Column(Integer(), ForeignKey('patients.id'))
    medication_id = Column(Integer(), ForeignKey('medications.id'))
    patient = relationship('Patient', back_populates='prescriptions')
    medication = relationship('Medication', back_populates='prescriptions')


def create_tables():
    # create the engine and tables based on parent base
    engine = create_engine('sqlite:///pharmacy.db')
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_tables()

    # with Session(engine) as session:
        # allopurinol = Medication(
        #     name ="Allopurinol",
        #     dosage ="100 mg",
        #     quantity = 90,
        #     price = 10.00
        #     )
        # session.add(allopurinol)
        # session.commit()

        # pantoprazole = Medication(
        #     name="Pantoprazole",
        #     dosage="40 mg",
        #     quantity=90,
        #     price=5.00
        # )
        # session.add(pantoprazole)
        # session.commit()

        # allmeds = session.query(Medication).all()
        # print(allmeds)

        # Prescription.__table__.drop(engine)

# now things we can do within our Session: CRUD
    # '''
    # Session.add()
    # Session.query()
    #     .all()
    #     .orderyby() ex Table.name.desc OR asc()
    #     .limit()
    #     .filter() ex Table.name = "name"
    #     .update() ex {Table.name: newname}
    # Session.delete()
    # Session.commit()
    # '''
