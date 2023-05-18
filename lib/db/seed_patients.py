# to populate patient database: from lib/db run => python3 seed_patients.py

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from faker import Faker
from models import Patient

fake = Faker()

engine = create_engine('sqlite:///pharmacy.db')
with Session(engine) as session:

    for i in range(100):
        newPatient = Patient(
            last_name=fake.last_name(),
            first_name=fake.first_name(),
            address=fake.address(),
            password=fake.password()
        )
        session.add(newPatient)
        session.commit()
        session.close()
