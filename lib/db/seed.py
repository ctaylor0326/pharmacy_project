from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from faker import Faker
from faker.providers import person, address 
from random import randint
from models import Medication, Patient

fake = Faker()

engine = create_engine('sqlite:///pharmacy.db')
with Session(engine) as session:
    for i in range(100):
        newPatient = Patient(
            last_name = fake.last_name(),
            first_name = fake.first_name(),
            address = fake.address()
        )
        session.add(newPatient)
        session.commit()
