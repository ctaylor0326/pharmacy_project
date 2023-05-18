# to populate medication database: from lib/db run => python3 seed_medications.py

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from faker import Faker
from faker.providers import person, address 
# from random import randint
from models import Medication

fake = Faker()

engine = create_engine('sqlite:///pharmacy.db')
with Session(engine) as session:

    medList = [
        Medication(
            name="Pantoprazole",
            type="proton pump inhibitor",
            dosage="40 mg",
            quantity=90,
            price=5.00),
        Medication(
            name="Allopurinol",
            type="xanthine oxidase inhibitor",
            dosage="100 mg",
            quantity=90,
            price=13.00),
        Medication(
            name="Azithromycin",
            type="antibiotic",
            dosage="250 mg",
            quantity=7,
            price=15.50)
        ]
    for med in medList:
        session.add(med)
        session.commit()

