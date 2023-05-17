from helpers import *
from db.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///pharmacy.db')
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    print(greeting_image)
    print()
    print('W e l c o m e   t o   W a l g r e e n z !')
    print()

    # retrieve patient object from the DB
    patient = None
    while not patient:
        patient_id = input('Please enter your patient ID: ')
        patient = session.query(Patient).filter(Patient.id == patient_id).one_or_none()
        

    # display patient info
    print()
    print()
    print()
    print()
    print(f'Welcome back, {patient.first_name} {patient.last_name}!')
    print()
    print(f"Your prescriptions on file are:")
    print('-' * 50)

    # display prescription table
    create_prescription_table(patient)

    # display fill prescription menu
    fill_prescription_menu()