# to populate patient database: from lib/db run => python3 seed_patients.py

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from faker import Faker
from models import Patient

fake = Faker()


engine = create_engine('sqlite:///pharmacy.db')
session = Session(engine)

for _ in range(100):
    last_name = fake.last_name()
    first_name = fake.first_name()
    username = f"{last_name.lower()}{first_name[:3].lower()}"
    new_patient = Patient(
        last_name=last_name,
        first_name=first_name,
        address=fake.address(),
        username=username,
        password=fake.password()
    )
    session.add(new_patient)
session.commit()
        
