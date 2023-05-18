import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Patient, Medication, Prescription
import ipdb
engine = create_engine('sqlite:///pharmacy.db')
Session = sessionmaker(bind=engine)


def generate_prescriptions():
    session = Session()

    patients = session.query(Patient).all()
    medications = session.query(Medication).all()

    for patient in patients:
        # Generate a random number of prescriptions for the patient
        num_prescriptions = random.randint(1, 5)  # Adjust the range as desired

        for _ in range(num_prescriptions):
            # Select a random medication from the medications table
            random_medication = random.choice(medications)

            # Create a prescription object linking the patient and medication
            prescription = Prescription(
                patient=patient, medication=random_medication)

            # Add the prescription to the session
            session.add(prescription)

    # Commit the changes and close the session
    session.commit()
    session.close()


generate_prescriptions()
