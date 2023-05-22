# to populate medication database: from lib/db run => python3 seed_medications.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Medication

engine = create_engine('sqlite:///pharmacy.db')
Session = sessionmaker(bind=engine)

med_list = [
    Medication(name="Pantoprazole", type="proton pump inhibitor", dosage="40 mg", quantity=90, price=5.00),
    Medication(name="Allopurinol", type="xanthine oxidase inhibitor", dosage="100 mg", quantity=90, price=13.00),
    Medication(name="Azithromycin", type="antibiotic", dosage="250 mg", quantity=7, price=15.50),
    Medication(name="Gentamicin", type="antibiotic", dosage="40 mg", quantity=10, price=11.00),
    Medication(name="Banzel", type="anti-epileptic", dosage="400 mg", quantity=15, price=15.00),
    Medication(name="Norco", type="Acetaminophen-hydrocodone", dosage="300 mg", quantity=8, price=22.00),
    Medication(name="Valium", type="benzodiazepine", dosage="10 mg", quantity=30, price=25.00),
    Medication(name="Lexapro", type="antidepressant", dosage="15 mg", quantity=15, price=40.00),
    Medication(name="Dexamethasone", type="corticosteroid ", dosage="1 mg", quantity=20, price=35.00),
    Medication(name="Harvoni", type="antiviral", dosage="1000 mg", quantity=60, price=8.00),
    Medication(name="Senokot", type="Laxatives", dosage="15 mg", quantity=25, price=20.00),
    Medication(name="Paxil", type="anti-depressant", dosage="10 mg", quantity=10, price=17.90),
    Medication(name="Buprenex", type="Opioids (narcotic analgesics)", dosage=".6 mg", quantity=12, price=18.90),
    Medication(name="Genotropin", type="Growth hormones", dosage=".33 mg", quantity=8, price=17.50),
    Medication(name="Medrol", type="steroid", dosage="4-48 mg", quantity=14, price=100.00),
    Medication(name="Hydrocortisone", type="steroid", dosage="10 mg", quantity=21, price=65.00),
    Medication(name="Keflex", type="antibiotic", dosage="500 mg", quantity=36, price=55.50),
    Medication(name="Opdivo", type="cancer medication", dosage="10 mg", quantity=52, price=72.70),
    Medication(name="Janumet", type="antidiabetic", dosage="100 mg", quantity=60, price=18.00),
    Medication(name="Glipizide", type="diaebetic", dosage="10 mg", quantity=24, price=19.00),
    Medication(name="Lantus", type="diabetic", dosage="100[iU] in 1mL", quantity=32, price=12.50),
    Medication(name="Pradaxa", type="anticoagulant", dosage="150 mg", quantity=36, price=14.50),
    Medication(name="Celebrex", type="nonsteroidal anti-inflammatory drug", dosage="200 mg", quantity=14, price=20.00),
    Medication(name="Yervoy", type="cancer medicine", dosage="4, 3mg", quantity=20, price=23.50),
    Medication(name="Flutamide", type="nonsteroidal antiandrogen", dosage="250", quantity=30, price=16.00)
]

with Session() as session:
    session.bulk_save_objects(med_list)
    session.commit()