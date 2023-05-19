import subprocess, os
from ascii import *
from db.otc import *
from db.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import click
from tabulate import tabulate
import time
import sys

# Get the absolute path to the directory containing the cli.py file
base_dir = os.path.abspath(os.path.dirname(__file__))
# Construct the path to the database file
pharmdb_path = os.path.join(base_dir, '/home/s0079376/Development/code/phase-3/Project/pharmacy_project/lib/db/pharmacy.db')
pharmacy_engine = create_engine(f'sqlite:///{pharmdb_path}')

otcdb_path = os.path.join(base_dir, 'otc.db')
otc_engine = create_engine(f'sqlite:///{otcdb_path}')

OTCSession = sessionmaker(bind=otc_engine)
PharmSession = sessionmaker(bind=pharmacy_engine)
# session1 = PharmSession()
#   -OR-
# session2 = OTCSession()


#//////////////////////////////////////////////////////////////
#////                                 style and formatting ////
#//////////////////////////////////////////////////////////////
def check_db_path():
    phdb_path = '/home/s0079376/Development/code/phase-3/Project/pharmacy_project/lib/db/pharmacy.db'
    print("Database file path:", phdb_path)
    if os.path.isfile(phdb_path):
        print("Database file exists")
    else:   
        print("Database file does not exist") 

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


def print_16_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.16)
        # time.sleep(0)
    print()


#//////////////////////////////////////////////////////////////
#////                                      display tables  ////
#//////////////////////////////////////////////////////////////


# def display_otc_table():
#     otc_items = session.query(Otc).all()
#     otc_items_list = [o for o in otc_items]

#     table = tabulate([otc_items_list], headers=['Name', 'category', 'Price'], tablefmt='mixed_grid')
#     click.echo(click.style((table), bold=True, bg="white", fg="black"))
#     print(table)


#//////////////////////////////////////////////////////////////
#////                                            pre menu  ////
#//////////////////////////////////////////////////////////////


def pre_menu():
        click.clear()
        print()
        print('-' * 50)
        print(walgreenz_image)
        print_1_slowly(greeting_image)
        print()
        print_4_slowly('W e l c o m e  t o  W a l g r e e n z !')
        print('-' * 50)
        print_8_slowly('.' * 50)
        main_menu()
    

#//////////////////////////////////////////////////////////////
#////                                           main menu  ////
#//////////////////////////////////////////////////////////////


def main_menu():
        click.clear()
        print_1_slowly(main_menu_image)       
        print('-' * 50)
        print()
        print_1_slowly("1.|   L o g i n")
        print_1_slowly("2.|   S i g n   U p")
        print_1_slowly("3.|   O v e r   t h e   C o u n t e r")
        print_1_slowly("4.|   S h o p p i n g   C a r t")
        print_1_slowly("5.|   D r.  W a l g z b o t")
        print_1_slowly("6.|   E X I T")
        print()
        print('-' * 50)
        print()
        main_menu_input = input("Please enter a number from the menu above: ")
        print('-' * 50)

        if main_menu_input == '1':
            login()

        elif main_menu_input == '2':
             sign_up()

        elif main_menu_input == '3':
             otc_menu()

        elif main_menu_input == '4':
            shopping_cart()

        elif main_menu_input == '5':
            click.clear()
            print(walgzbot_image)
            print('-' * 50)
            print()
            subprocess.run(['python', 'lib/walgzbot.py'])

        elif main_menu_input == '6':
            click.clear()
            print(walgreenz_image)
            print_4_slowly('T h a n k   y o u   f o r   c h o o s i n g   W a l g r e e n z !')
            print_8_slowly("                    G o o d b y e !")
            exit()

        else:
            print('Invalid choice. Please try again.')


#//////////////////////////////////////////////////////////////
#////                                   for existing user  ////
#//////////////////////////////////////////////////////////////

#//////////////////////////  login  ////

def login():
        click.clear()
        print_1_slowly(login_image)
        print('-' * 50)
        print()
        username = input('Please  enter  your  USERNAME: ')
        password = input('Please enter your PASSWORD: ')
        print()
        print_1_slowly('You are being logged in!')
        print_4_slowly(".........................................")
        session1 = PharmSession()
        try:
            patient = session1.query(Patient).filter_by(username=username, password=password).one()
          
            print("Login successful!")
            print(f"Welcome, {patient.first_name} {patient.last_name}!")
            user_login_greeting(session1, patient)

        except NoResultFound:
            print("Invalid login credentials. Please Sign Up.")
            print("You are being redirected to the Main Menu")
            print_4_slowly("." * 50)
            main_menu()
        print()

#//////////////////////////  user login greeting  ////

def user_login_greeting(session1, patient):
        click.clear()
        print_1_slowly(welcome_back_image)
        print()
        print('-' * 50)
        print()
        print_4_slowly(f'Welcome back, {patient.first_name} {patient.last_name}!')
        print()
        print_4_slowly("How can we help you today?")
        print()
        print()
        print_4_slowly("1. View my prescriptions.")
        print()
        print_4_slowly("2. Browse OTC medications.")
        print('-' * 50)
        print()
        user_login_greeting_input = input('Please enter 1 or 2 to select your option: ')
        print()
        print('-' * 50)

        if user_login_greeting_input == '1':
            user_rx(session1, patient)

        elif user_login_greeting_input == '2':
            print("You are being redirected to the OTC Menu")
            print_4_slowly("." * 50)
            otc_menu(session1, patient)

        else:
            print('-' * 50)
            print()
            print('Invalid choice. Please try again.')
            print()
            print('-' * 50)


#////////////////////////////////////////////  user prescription screen ////

#directed from user_login_greeting 
def user_rx(session1, patient):
    click.clear()
    print_1_slowly(prescriptions_image)
    print('-' * 50)
    print()
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
        print_1_slowly('Would you like to fill any of your prescriptions today?')
        print()
        print('-' * 50)
        user_rx_input = input('Please enter the number of the medication or 0 to cancel: ')

        if user_rx_input.isdigit():
            medication_index = int(user_rx_input)
            if 1 <= medication_index <= len(medications_list):
                rx_menu_input_yes(session1, patient)
            elif medication_index == 0:
                print()
                print_1_slowly('You have canceled the prescription fill.')
                print()
                print_8_slowly('Thank you for choosing Walgreenz!')
                print()
                print('-' * 50)
                print("You are being redirected to the Previous Menu")
                print_4_slowly(".........................................")
                user_login_greeting(session1, patient)
            else:
                print('Invalid medication number. Please try again.')
        else:
            print('Invalid input. Please try again.')
    else:
        # If no prescriptions are found for the patient
        print_4_slowly("You have no prescriptions on file.")
        print()
        print_4_slowly("Thank you for choosing Walgreenz!")
        print()
        print('-' * 50)
        print("You are being redirected to the Main Menu")
        print_4_slowly(".........................................")
        main_menu()



# def second_menu_input_yes(medication):
def rx_menu_input_yes(session1, patient):
        print()
        print()
        print_8_slowly('Your prescriptions will be ready for pick up in 45 minutes.')
        print()
        print_4_slowly('Thank you for choosing Walgreenz!')
        print()
        print_4_slowly("." * 50)
        user_rx(session1, patient)


#//////////////////////////////////////////////////////////////
#////                                             Sign up  ////
#//////////////////////////////////////////////////////////////


def sign_up():
        click.clear()
        print_1_slowly(sign_up_image)
        print('-' * 50)
        print()
        input('Please  create  your  LOGIN: ')
        input('Please create your PASSWORD: ')
        # while not patient:
            # patient_id = input('Please enter your patient ID: ')
            # patient = session.query(Patient).filter(Patient.id == patient_id).one_or_none()
        print_1_slowly('Your account is being created!')
        print_4_slowly(".........................................")
        print_1_slowly("Account created!")
        print("you are being redirected to the login page")
        print_8_slowly(".........................................")
        # user_greeting(patient)
        login()


#//////////////////////////////////////////////////////////////
#////                                Over the counter menu ////
#//////////////////////////////////////////////////////////////


def otc_menu(session1, patient):
    click.clear()
    print_1_slowly(over_the_counter_image)
    print('-' * 50)
    print()
    print_1_slowly("1.|   P a i n   R e l i e f")
    print_1_slowly("2.|   A l l e r g y   R e l i e f")
    print_1_slowly("3.|   C o l d   &   F l u")
    print_1_slowly("4.|   S e e   A l l") 
    print_1_slowly("5.|   S h o p p i n g   C a r t")
    print_1_slowly("6.|   M a i n   M e n u")
    print_1_slowly("7.|   E X I T")
    print()
    print('-' * 50)
    print()
    otc_menu_input = input("Please enter a number from the menu above: ")

    if otc_menu_input == '1':
        pain_relief()

    elif otc_menu_input == '2':
        allergy_relief()

    elif otc_menu_input == '3':
        cold_and_flu()

    elif otc_menu_input == '4':
        see_all_otc()

    elif otc_menu_input == '5':
        shopping_cart()

    elif otc_menu_input == '6':
        main_menu()

    elif otc_menu_input == '7':
        click.clear()
        print(walgreenz_image)
        print_4_slowly('T h a n k   y o u   f o r   c h o o s i n g   W a l g r e e n z !')
        print_8_slowly("                    G o o d b y e !")
        exit()

    else:
        print('Invalid choice. Please try again.')

#//////////////////////////////////////////////////////////////
#////                            otc items display options ////
#//////////////////////////////////////////////////////////////

#//////////////////////pain relief////

def pain_relief():
    click.clear()
    print_1_slowly(pain_relief_image)
    print('-' * 67)
    print(f'| ID |{" " * 8}ITEM NAME{" " * 8}|{" " * 8}CATEGORY{" " * 8}|  PRICE  |')
    print('-' * 67)

    otc_items = session.query(Otc).filter_by(category = "Pain Reliever").all()

    for otc_item in otc_items:
        id_spaces = 4 - len(str(otc_item.id))
        name_spaces = 26 - len(otc_item.name)
        category_spaces = 24 - len(otc_item.category)
        price_spaces = 8 - len(f'{otc_item.price:.2f}')
        output_string = f'|{otc_item.id}{" " * id_spaces}|' + \
        f'{otc_item.name}{" " * name_spaces}|' + \
        f'{otc_item.category}{" " * category_spaces}|' + \
        f'${otc_item.price:.2f}{" " * price_spaces}|'
        print(output_string)

    print('-' * 50)

    otc_fill_cart(session, otc_item)

#//////////////////////allergy relief////

def allergy_relief():
    click.clear()
    print_1_slowly(allergy_image)
    print('-' * 67)
    print(f'| ID |{" " * 8}ITEM NAME{" " * 8}|{" " * 8}CATEGORY{" " * 8}|  PRICE  |')
    print('-' * 67)

    otc_items = session.query(Otc).filter_by(category = "Allergy").all()

    for otc_item in otc_items:
        id_spaces = 4 - len(str(otc_item.id))
        name_spaces = 26 - len(otc_item.name)
        category_spaces = 24 - len(otc_item.category)
        price_spaces = 8 - len(f'{otc_item.price:.2f}')
        output_string = f'|{otc_item.id}{" " * id_spaces}|' + \
        f'{otc_item.name}{" " * name_spaces}|' + \
        f'{otc_item.category}{" " * category_spaces}|' + \
        f'${otc_item.price:.2f}{" " * price_spaces}|'
        print(output_string)
    
    print('-' * 50)

    otc_fill_cart(session, otc_item)

#//////////////////////cold & flu////

def cold_and_flu():
    click.clear()
    print_1_slowly(cold_and_flu_image)
    print('-' * 70)
    print(f'| ID |{" " * 8}ITEM NAME{" " * 8}|{" " * 8}CATEGORY{" " * 8}|  PRICE  |')
    print('-' * 70)

    otc_items = session.query(Otc).filter_by(category = "Cold & Flu").all()

    for otc_item in otc_items:
        id_spaces = 4 - len(str(otc_item.id))
        name_spaces = 26 - len(otc_item.name)
        category_spaces = 24 - len(otc_item.category)
        price_spaces = 8 - len(f'{otc_item.price:.2f}')
        output_string = f'|{otc_item.id}{" " * id_spaces}|' + \
        f'{otc_item.name}{" " * name_spaces}|' + \
        f'{otc_item.category}{" " * category_spaces}|' + \
        f'${otc_item.price:.2f}{" " * price_spaces}|'
        print(output_string)
    
    print('-' * 50)

    otc_fill_cart(session, otc_item)

#//////////////////////see all otc items////

def see_all_otc():
    click.clear()
    print_1_slowly(all_items_image)   
    print('-' * 67)
    print(f'| ID |{" " * 8}ITEM NAME{" " * 8}|{" " * 8}CATEGORY{" " * 8}|  PRICE  |')
    print('-' * 67)

    otc_items = session.query(Otc).all()

    for otc_item in otc_items:
        id_spaces = 4 - len(str(otc_item.id))
        name_spaces = 26 - len(otc_item.name)
        category_spaces = 24 - len(otc_item.category)
        price_spaces = 8 - len(f'{otc_item.price:.2f}')
        output_string = f'|{otc_item.id}{" " * id_spaces}|' + \
        f'{otc_item.name}{" " * name_spaces}|' + \
        f'{otc_item.category}{" " * category_spaces}|' + \
        f'${otc_item.price:.2f}{" " * price_spaces}|'
        print(output_string)
    
    print('-' * 50)

    otc_fill_cart(session, otc_item)

#//////////////////////////////////////////////////////////////
#////                                            fill cart ////
#//////////////////////////////////////////////////////////////

def otc_fill_cart(session, otc_item):
    shopping_cart = ShoppingCart()
    otc_item_id = input('Please enter the ID of the item you would like to add to your cart: ')
    cart_total = 0
    while otc_item_id:
        otc_item = session.query(Otc).filter(Otc.id == otc_item_id).one_or_none()
        if otc_item:
            cart_total += otc_item.price
            print(f'Your cart total is ${cart_total:.2f}')
            otc_item_id = input('Please enter the ID of the item you would like to add to your cart: ')
        else:
            print('Invalid ID. Please try again.')
            otc_item_id = input('Please enter the ID of the item you would like to add to your cart: ')

    print()
    print('-' * 50)
    print()
    fill_cart_menu_input = input('Please enter 1 to return to the main menu or 2 to exit: ')
    print()
    print('-' * 50)

    if fill_cart_menu_input == '1':
        main_menu()
    
    elif fill_cart_menu_input == '2':
        click.clear()
        print(walgreenz_image)
        print_4_slowly('T h a n k   y o u   f o r   c h o o s i n g   W a l g r e e n z !')
        print_8_slowly("                    G o o d b y e !")
        exit()

    else:
        print('Invalid choice. Please try again.')

#//////////////////////////////////////////////////////////////
#////                                        shopping cart ////
#//////////////////////////////////////////////////////////////

def shopping_cart():
    click.clear()
    print_1_slowly(shopping_cart_image)
    print('-' * 50)
    print()
    print('-' * 67)
    print(f'| ID |{" " * 8}ITEM NAME{" " * 8}|{" " * 8}CATEGORY{" " * 8}|  PRICE  |')
    print('-' * 67)
    shopping_cart_input = input('enter 1 for Main Menu or 2 for Exit: ')
     
    if shopping_cart_input == '1':
          main_menu()

    elif shopping_cart_input == '2':
        click.clear()
        print(walgreenz_image)
        print_4_slowly('T h a n k   y o u   f o r   c h o o s i n g   W a l g r e e n z !')
        print_8_slowly("                    G o o d b y e !")
        exit()

    else:
        print('Invalid choice. Please try again.')


#/////////////////////////////////////////////////////////////
#////                                    Welcome to Walgreenz!
#/////////////////////////////////////////////////////////////


if __name__ == '__main__':
    # check_db_path()
    pre_menu()