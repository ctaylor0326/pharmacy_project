import random
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from models import Patient, Medication, Prescription

engine = create_engine('sqlite:///pharmacy.db')
Session = sessionmaker(bind=engine)

def generate_prescriptions():
    with Session() as session:
        patients = session.query(Patient).all()
        medications = session.query(Medication).all()

        for patient in patients:
            num_prescriptions = random.randint(1, 5)

            # Select a random sample of medications without replacement
            random_medications = random.sample(medications, num_prescriptions)

            prescriptions = [
                Prescription(patient=patient, medication=medication)
                for medication in random_medications
            ]

            # Add the prescriptions to the session
            session.add_all(prescriptions)

        session.commit()

generate_prescriptions()
