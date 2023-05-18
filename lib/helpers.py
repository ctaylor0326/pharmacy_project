from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.models import *

engine = create_engine('sqlite:///pharmacy.db')
Session = sessionmaker(bind=engine)
session = Session()
