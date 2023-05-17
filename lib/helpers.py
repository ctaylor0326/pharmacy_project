from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.models import *

engine = create_engine('sqlite:///pharmacy.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_prescription_table(patient):

    # retrieve orders for the patient ID

    
    #print table header
    header = f"{'ID':<5}{'Medication':<15}{'Dosage':<10}{'Quantity':<10}{'Price':<10}"
    print(header)
    print('-' * len(header))

    # print table rows
    row = f"{prescription.id:<5}{prescription.name:<15}{prescription.dosage:<10}{prescription.quantity:<10}{prescription.price:<10}"
    print(row)

    print('-' * len(header))


    # pass prescription id to fill prescription menu


def fill_prescription_menu():
    while True:
        print('1. Fill prescription')
        print('2. Cancel prescription')
        print('3. Exit')
        choice = input()

        if choice == '1':
            # set prescription pick up time
            print('Thank you for your order! Your prescriptions will be ready for pick up in 15 minutes.')
            print(walgreenz_image)
            break

        elif choice == '2':
            # cancel prescription
            print('Your prescription has been cancelled.')
            print("Thank you for choosing Walgreenz!")
            print(walgreenz_image)
            break

        elif choice == '3':
            # exit
            print('Your prescription will not be filled.')
            print("Thank you for choosing Walgreenz!")
            print(walgreenz_image)
            break

        else:
            # invalid choice
            print('Invalid choice. Please try again.')




greeting_image = """
              _________
             {_________}
              )=======(
             |         |
            | _________ |
            ||   _     ||
            ||  |_)    ||
            ||  | \/   ||
      __    ||    /\   ||
 __  (_|)   |'---------'|
(_|)        `-.........-'
"""

walgreenz_image = """

 _       __      __                              
| |     / /___ _/ /___ _________  ___  ____  ____
| | /| / / __ `/ / __ `/ ___/ _ \/ _ \/ __ \/_  /
| |/ |/ / /_/ / / /_/ / /  /  __/  __/ / / / / /_
|__/|__/\__,_/_/\__, /_/   \___/\___/_/ /_/ /___/
               /____/                            
"""