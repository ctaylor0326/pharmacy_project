import subprocess, os
from ascii import *
from ascii_ani import *
from db.otc import *
from db.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import click
import time
from time import sleep
import sys

# Get the absolute path to the directory containing the cli.py file
base_dir = os.path.abspath(os.path.dirname(__file__))
# Construct the path to the database file
pharmdb_path = os.path.join(base_dir, '/Users/mattroche/Development/code/phase-3/pharmacy_project/lib/db/pharmacy.db')
pharmacy_engine = create_engine(f'sqlite:///{pharmdb_path}')

otcdb_path = os.path.join(base_dir, 'otc.db')
otc_engine = create_engine(f'sqlite:///{otcdb_path}')

OTCSession = sessionmaker(bind=otc_engine)
PharmSession = sessionmaker(bind=pharmacy_engine)
# session1 = PharmSession()
#   -OR-
# session2 = OTCSession()


def check_db_path():
    phdb_path = '/Users/mattroche/Development/code/phase-3/pharmacy_project/lib/db/pharmacy.db'
    print("Database file path:", phdb_path)
    if os.path.isfile(phdb_path):
        print("Database file exists")
    else:   
        print("Database file does not exist") 


#//////////////////////////////////////////////////////////////
#////                                 text style           ////
#//////////////////////////////////////////////////////////////


def print_1_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.01)
        # time.sleep(0)
    print()


def print_4_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.04)
        # time.sleep(0)
    print()


def print_8_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.08)
        # time.sleep(0)
    print()


#//////////////////////////////////////////////////////////////
#////                                            pre menu  ////
#//////////////////////////////////////////////////////////////


def pre_menu():
        click.clear()
        print()
        print('-' * 50)
        pre_menu_ani()
        print()
        print_4_slowly('      W e l c o m e  t o  W a l g r e e n z !')
        print('-' * 50)
        main_menu()
    

#//////////////////////////////////////////////////////////////
#////                                           main menu  ////
#//////////////////////////////////////////////////////////////


def main_menu():
        shopping_cart = []
        click.clear()
        print_1_slowly(main_menu_image)      
        print('-' * 50)
        print()
        print("      1.|   Login")
        sleep(0.04)
        print("      2.|   Sign Up")
        sleep(0.04)
        print("      3.|   Dr. Walgzbot")
        sleep(0.04)
        print("      4.|   EXIT")
        print()
        print('-' * 50)
        sleep(0.04)
        main_menu_input = input(" Please enter number from the menu above: ")
        print('-' * 50)

        if main_menu_input == '1':
            login(shopping_cart)

        elif main_menu_input == '2':
             sign_up(shopping_cart)

        elif main_menu_input == '3':
            click.clear()
            print(walgzbot_image)
            print('-' * 50)
            print()
            subprocess.run(['python', 'lib/walgzbot.py'])

        elif main_menu_input == '4':
            click.clear()
            print(walgreenz_image)
            print_4_slowly(' Thank you for choosing Walgreenz!')
            print_8_slowly("                    G o o d b y e !")
            exit()

        else:
            print(' Invalid choice. Please try again.')


#//////////////////////////////////////////////////////////////
#////                                          user login  ////
#//////////////////////////////////////////////////////////////


def login(shopping_cart):
        click.clear()
        print_1_slowly(login_image)
        print('-' * 50)
        print()
        username = input(' Please  enter  your  USERNAME: ')
        password = input(' Please enter your PASSWORD: ')
        print()
        print_1_slowly(' You are being logged in!')
        print_4_slowly(".........................................")
        session1 = PharmSession()
        session2 = OTCSession()
        try:
            patient = session1.query(Patient).filter_by(username=username, password=password).one()
          
            print(" Login successful!")
            print(f" Welcome, {patient.first_name} {patient.last_name}!")
            user_login_greeting(session1, session2, patient, shopping_cart)

        except NoResultFound:
            print(" Invalid login credentials. Please Sign Up.")
            print(" You are being redirected to the Main Menu")
            print_4_slowly("." * 50)
            main_menu()
        print()

#//////////////////////////////////////////////////////////////
#////                 user login greeting "Welcome Back!"  ////
#//////////////////////////////////////////////////////////////

def user_login_greeting(session1, session2, patient, shopping_cart):
        click.clear()
        print_1_slowly(welcome_back_image)
        print()
        print('-' * 50)
        print()
        print_4_slowly(f' How can we help you today, {patient.first_name} {patient.last_name}?')
        print()
        print("      1.|   View my prescriptions.")
        sleep(0.04)
        print("      2.|   Browse OTC medications.")
        sleep(0.04)
        print("      3.|   View my shopping cart.")
        sleep(0.04)
        print("      4.|   Dr. Walgzbot")
        sleep(0.04)
        print("      5.|   Main Menu.")
        print()
        print('-' * 50)
        sleep(0.04)
        user_login_greeting_input = input(' Please enter number from the menu above: ')

        if user_login_greeting_input == '1':
            user_rx(session1, session2, patient,shopping_cart)

        elif user_login_greeting_input == '2':
            otc_menu(session1, session2, patient,shopping_cart)

        elif user_login_greeting_input == '3':
            check_out(session1, session2, patient, shopping_cart)

        elif user_login_greeting_input == '4':
            click.clear()
            print(walgzbot_image)
            print('-' * 50)
            print()
            subprocess.run(['/Users/mattroche/Development/code/phase-3/pharmacy_project/lib/walgzbot.py'])

        elif user_login_greeting_input == '5':
            session1.close()
            main_menu()

        else:
            print('-' * 50)
            print()
            print(' Invalid choice. Please try again.')
            print()
            print('-' * 50)


#////////////////////////////////////////////  user prescription screen ////

#directed from user_login_greeting 
def user_rx(session1, session2, patient, shopping_cart):
    click.clear()
    print_1_slowly(prescriptions_image)
    print('-' * 50)
    print()

    # Retrieve the patient's prescriptions
    prescriptions = session1.query(Prescription).filter(Prescription.patient_id == patient.id).all()

    if prescriptions:
        # Create a numbered list of medications
        medications_list = []
        for index, prescription in enumerate(prescriptions, start=1):
            medication = session1.query(Medication).filter(Medication.id == prescription.medication_id).one_or_none()
            if medication:
                medication_info = f'{medication.name} {medication.type} {medication.dosage} {medication.quantity} {medication.price}'
                medications_list.append(f'{index}. {medication_info}')

        # Print the numbered list of medications
        for medication_item in medications_list:
            print_4_slowly(medication_item)
            print()

        # After printing the medications, prompt the user for further actions
        print('-' * 50)
        print_4_slowly(' Would you like to fill any of your prescriptions today?')
        print()
        print('-' * 50)
        user_rx_input = input(' Please enter number of the medication or 0 to cancel: ')

        if user_rx_input.isdigit():
            medication_index = int(user_rx_input)
            if 1 <= medication_index <= len(medications_list):
                rx_menu_input_yes(session1, session2, patient, shopping_cart)
            elif medication_index == 0:
                print()
                print_1_slowly(' You have cancelled the prescription fill.')
                print()
                print('-' * 50)
                print(" You are being redirected to the Previous Menu")
                print_4_slowly(".........................................")
                user_login_greeting(session1, session2, patient, shopping_cart)
            else:
                print(' Invalid medication number. Please try again.')
        else:
            print(' Invalid input. Please try again.')
    else:
        # If no prescriptions are found for the patient
        print_4_slowly("    You have no prescriptions on file.")
        print()
        print_4_slowly("Thank you for choosing Walgreenz!")
        print()
        print('-' * 50)
        print("You are being redirected to the Previous Menu")
        print_4_slowly(".........................................")
        user_login_greeting(session1, session2, patient, shopping_cart)

# def second_menu_input_yes(medication):
def rx_menu_input_yes(session1, session2, patient, shopping_cart):
        print()
        print()
        print_4_slowly('  Your prescriptions will be ready for pick up in 45 minutes.')
        print()
        print_4_slowly('    Thank you for choosing Walgreenz!')
        print()
        print_4_slowly("." * 50)
        user_rx(session1, session2, patient, shopping_cart)


#//////////////////////////////////////////////////////////////
#////                                             Sign up  ////
#//////////////////////////////////////////////////////////////


def sign_up(shopping_cart):
    click.clear()
    print_1_slowly(sign_up_image)
    print('-' * 50)
    print()
    username = input(' Please enter your USERNAME: ')
    password = input(' Please enter your PASSWORD: ')
    address = input(' Please enter your ADDRESS: ')
    first_name = input(' Please enter your First Name: ')
    last_name = input(' Please enter your Last Name: ')

    new_patient = Patient(username=username, password=password, address=address, first_name=first_name, last_name=last_name)

    session1 = PharmSession()
    session2 = OTCSession()
    try:
        session1.add(new_patient)
        session1.commit()
        print_1_slowly('  Creating your account!')
        print_4_slowly("." * 42)
        print("        Account created!")
        print_8_slowly("." * 42)
        patient = session1.query(Patient).filter_by(username=username, password=password).one()
    except Exception as e:
        session1.rollback()
        print(" Error creating the account:", str(e))
    finally:
        user_login_greeting(session1, session2, patient, shopping_cart)


#//////////////////////////////////////////////////////////////
#////                                Over the counter menu ////
#//////////////////////////////////////////////////////////////


def otc_menu(session1, session2, patient, shopping_cart):
    click.clear()
    print_1_slowly(over_the_counter_image)
    print('-' * 50)
    print()
    print("      1.|   Pain Relief")
    sleep(0.06)
    print("      2.|   Allergy Relief")
    sleep(0.06)
    print("      3.|   Cold & Flu")
    sleep(0.06)
    print("      4.|   See All") 
    sleep(0.06)
    print("      5.|   Shopping Cart")
    sleep(0.06)
    print("      6.|   Return to Previous Menu")
    sleep(0.06)
    print("      7.|   EXIT")
    print()
    print('-' * 50)
    sleep(0.06)
    otc_menu_input = input(" Please enter number from the menu above: ")

    if otc_menu_input == '1':
        pain_relief(session1, session2, patient, shopping_cart)

    elif otc_menu_input == '2':
        allergy_relief(session1, session2, patient, shopping_cart)

    elif otc_menu_input == '3':
        cold_and_flu(session1, session2, patient, shopping_cart)

    elif otc_menu_input == '4':
        see_all_otc(session1, session2, patient, shopping_cart)

    elif otc_menu_input == '5':
        shopping_cart(session1, session2, patient, shopping_cart)

    elif otc_menu_input == '6':
        user_login_greeting(session1, session2, patient, shopping_cart)

    elif otc_menu_input == '7':
        click.clear()
        print(walgreenz_image)
        print_4_slowly(' Thank you for choosing Walgreenz!')
        print_8_slowly("                    G o o d b y e !")
        exit()

    else:
        print(' Invalid choice. Please try again.')


#//////////////////////////////////////////////////////////////
#////                            otc items display options ////
#//////////////////////////////////////////////////////////////


#////////////////////////////////////////////////////////////////pain relief////

def pain_relief(session1, session2, patient, shopping_cart):
    click.clear()
    print_1_slowly(pain_relief_image)
    print('-' * 67)
    print(f'| ID |{" " * 8}ITEM NAME{" " * 8}|{" " * 5}CATEGORY{" " * 5}|  PRICE  |')
    print('-' * 67)

    otc_items = session2.query(Otc).filter_by(category="Pain Reliever").all()

    item_variables = {}

    for i, otc_item in enumerate(otc_items, start=1):
        name_spaces = 25 - len(otc_item.name)
        category_spaces = 18 - len(otc_item.category)
        price_spaces = 8 - len(f'{otc_item.price:.2f}')
        output_string = f'| {i:<3} |' + \
                        f'{otc_item.name}{" " * name_spaces}|' + \
                        f'{otc_item.category}{" " * category_spaces}|' + \
                        f' ${otc_item.price:.2f}{" " * price_spaces}|'
        print(output_string)

        item_variables[str(i)] = otc_item  # Assign each item to a variable based on its number

    print('-' * 67)

    user_input = input(" Please enter the number of the item you want to select: ")

    otc_item = item_variables.get(user_input)
    if otc_item is not None:
        print(f"You have selected: {otc_item.name}")
        shopping_cart.append(otc_item)
    else:
        print(" Invalid input. Please try again.")

    check_out(session1, session2, patient, shopping_cart)
    
#/////////////////////////////////////////////////////////////allergy relief////

def allergy_relief(session1, session2, patient, shopping_cart):
    click.clear()
    print_1_slowly(allergy_image)
    print('-' * 67)
    print(f'| ID |{" " * 8}ITEM NAME{" " * 8}|{" " * 5}CATEGORY{" " * 5}|  PRICE  |')
    print('-' * 67)

    otc_items = session2.query(Otc).filter_by(category = "Allergy").all()

    item_variables = {}

    for i, otc_item in enumerate(otc_items, start=1):
        name_spaces = 25 - len(otc_item.name)
        category_spaces = 18 - len(otc_item.category)
        price_spaces = 8 - len(f'{otc_item.price:.2f}')
        output_string = f'| {i:<3} |' + \
                        f'{otc_item.name}{" " * name_spaces}|' + \
                        f'{otc_item.category}{" " * category_spaces}|' + \
                        f' ${otc_item.price:.2f}{" " * price_spaces}|'
        print(output_string)

        item_variables[str(i)] = otc_item  # Assign each item to a variable based on its number

    print('-' * 67)

    user_input = input(" Please enter the number of the item you want to select: ")

    otc_item = item_variables.get(user_input)
    if otc_item is not None:
        print(f" You have selected: {otc_item.name}")
        shopping_cart.append(otc_item)
    else:
        print(" Invalid input. Please try again.")

    check_out(session1, session2, patient, shopping_cart)

#//////////////////////////////////////////////////////////////cold & flu////

def cold_and_flu(session1, session2, patient, shopping_cart):
    click.clear()
    print_1_slowly(cold_and_flu_image)
    print('-' * 70)
    print(f'| ID |{" " * 8}ITEM NAME{" " * 8}|{" " * 5}CATEGORY{" " * 5}|  PRICE  |')
    print('-' * 70)

    otc_items = session2.query(Otc).filter_by(category = "Cold & Flu").all()

    item_variables = {}

    for i, otc_item in enumerate(otc_items, start=1):
        name_spaces = 25 - len(otc_item.name)
        category_spaces = 18 - len(otc_item.category)
        price_spaces = 8 - len(f'{otc_item.price:.2f}')
        output_string = f'| {i:<3} |' + \
                        f'{otc_item.name}{" " * name_spaces}|' + \
                        f'{otc_item.category}{" " * category_spaces}|' + \
                        f' ${otc_item.price:.2f}{" " * price_spaces}|'
        print(output_string)

        item_variables[str(i)] = otc_item  # Assign each item to a variable based on its number

    print('-' * 67)

    user_input = input(" Please enter the number of the item you want to select: ")

    otc_item = item_variables.get(user_input)
    if otc_item is not None:
        print(f" You have selected: {otc_item.name}")
        shopping_cart.append(otc_item)
    else:
        print(" Invalid input. Please try again.")

    check_out(session1, session2, patient, shopping_cart)

#///////////////////////////////////////////////////////////see all otc items////

def see_all_otc(session1, session2, patient, shopping_cart):
    click.clear()
    print_1_slowly(all_items_image)   
    print('-' * 67)
    print(f'| ID |{" " * 8}ITEM NAME{" " * 8}|{" " * 5}CATEGORY{" " * 5}|  PRICE  |')
    print('-' * 67)

    otc_items = session2.query(Otc).all()

    item_variables = {}
    for i, otc_item in enumerate(otc_items, start=1):
        name_spaces = 25 - len(otc_item.name)
        category_spaces = 18 - len(otc_item.category)
        price_spaces = 8 - len(f'{otc_item.price:.2f}')
        output_string = f'| {i:<3} |' + \
                        f'{otc_item.name}{" " * name_spaces}|' + \
                        f'{otc_item.category}{" " * category_spaces}|' + \
                        f' ${otc_item.price:.2f}{" " * price_spaces}|'
        print(output_string)

        item_variables[str(i)] = otc_item  # Assign each item to a variable based on its number

    print('-' * 67)

    user_input = input(" Please enter the number of the item you want to select: ")

    otc_item = item_variables.get(user_input)
    if otc_item is not None:
        print(f" You have selected: {otc_item.name}")
        shopping_cart.append(otc_item)
    else:
        print(" Invalid input. Please try again.")

    check_out(session1, session2, patient, shopping_cart)


#//////////////////////////////////////////////////////////////
#////                                        shopping cart ////
#//////////////////////////////////////////////////////////////


def check_out(session1, session2, patient, shopping_cart):
    click.clear()
    print_1_slowly(shopping_cart_image)
    print()
    print('-' * 67)
    print(f'| ID |{" " * 8}ITEM NAME{" " * 8}|{" " * 8}CATEGORY{" " * 8}|  PRICE  |')
    print('-' * 67)
    
    total_price = 0
    
    for item in shopping_cart:
        print(f'| {item.id:<3}|{item.name:<25}|{item.category:<18}|${item.price:.2f}{" " * (8 - len(f"{item.price:.2f}"))}|')
        total_price += item.price
    
    print('-' * 67)
    print(f'{" " * 37}Total Price: ${total_price:.2f}')
    print()
    print()
    
    print('-' * 40)
    print("      1.|   Continue Browsing OTC Menu")
    sleep(0.04)
    print("      2.|   Return to Prescriptions")
    sleep(0.04)
    print("      3.|   Main Menu (you will be logged out)")
    print('-' * 50)
    shopping_cart_input = input(' Please enter number from the menu above: ')
     
    if shopping_cart_input == '1':
        otc_menu(session1, session2, patient, shopping_cart)

    if shopping_cart_input == '2':
        user_rx(session1, session2, patient, shopping_cart)

    elif shopping_cart_input == '3':
        click.clear()
        session1.close()
        session2.close()
        main_menu()

    else:
        print(' Invalid choice. Please try again.')


#/////////////////////////////////////////////////////////////
#////                                    Welcome to Walgreenz!
#/////////////////////////////////////////////////////////////


if __name__ == '__main__':
    # check_db_path()
    pre_menu()