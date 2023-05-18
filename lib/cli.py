import subprocess
from helpers import *
from ascii import *
from db.otc import *
from db.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import click
from tabulate import tabulate
import time
import sys

engine = create_engine('sqlite:///otc.db')
Session = sessionmaker(bind=engine)
session = Session()

#//////////////////////////////////////////////////////////////
#////                                 style and formatting ////
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
        input('Please  enter  your  LOGIN: ')
        input('Please enter your PASSWORD: ')
        print()
        print_1_slowly('You are being logged in!')
        print_4_slowly(".........................................")
        # while not patient:
            # patient_id = input('Please enter your patient ID: ')
            # patient = session.query(Patient).filter(Patient.id == patient_id).one_or_none()
        print()
        # user_greeting(patient)
        user_login_greeting()


#//////////////////////////  user login greeting  ////

# def user_login_greeting(patient):
def user_login_greeting():
        click.clear()
        print_1_slowly(welcome_back_image)
        print()
        print('-' * 50)
        print()
        # print_slowly(f'Welcome back, {patient.first_name} {patient.last_name}!')
        print_4_slowly(f'Welcome back, John Smith!')
        print()
    #retrieve patient prescriptions
        # script_on_file = session.query(Prescription).filter(Prescription.patient_id == patient.id).one_or_none()
        print_4_slowly("Would you like to see your prescriptions?")
        print()
        print('-' * 50)
        print()
        user_login_greeting_input = input('Please enter 1 for yes or 2 for no: ')
        print()
        print('-' * 50)

        if user_login_greeting_input == '1':
            # first_menu_input_yes(script_on_file)
            user_rx()

        elif user_login_greeting_input == '2':
            print('Thank you for choosing Walgreenz!')
            print("You are being redirected to the Main Menu")
            print_4_slowly("." * 50)
            main_menu()

        else:
            print('-' * 50)
            print()
            print('Invalid choice. Please try again.')
            print()
            print('-' * 50)


#////////////////////////////////////////////  user prescription screen ////

# def first_menu_input_yes(script_on_file):
def user_rx():
        click.clear()
        print_1_slowly(prescriptions_image)
        print('-' * 50)
        print()
        print()
        # medication = session.query(Medication).filter(Medication.id == script_on_file.prescription_id).one_or_none()
        # print(f'{medication.name} {medication.dosage} {medication.quantity} {medication.price}')
        print_4_slowly(f'1.|   Lipitor   |   20mg   |   30   |   $10.00   |')
        print()
        print()
        print('-' * 50)
        # print(f'Would you like to fill your prescription for {medication.name}?')
        print_1_slowly('Would you like to fill your prescription for Lipitor?')
        print()
        print('-' * 50)
        user_rx_input = input('Please enter 1 for yes or 2 for no: ')

        if user_rx_input == '1':
            # second_menu_input_yes(medication)
            rx_menu_input_yes()

        elif user_rx_input == '2':
            print('Your prescription will not be filled.')
            print()
            print_8_slowly('Thank you for choosing Walgreenz!')
            print()
            print('-' * 50)
            print("You are being redirected to the Main Menu")
            print_4_slowly(".........................................")
            main_menu()

        else:
            print('Invalid choice. Please try again.')


# def second_menu_input_yes(medication):
def rx_menu_input_yes():
        # print(f'Your {medication.name} prescriptions will be ready for pick up in 15 minutes.')
        print('Your Lipitor prescriptions will be ready for pick up in 45 minutes.')
        print()
        print_1_slowly('Thank you for choosing Walgreenz!')
        print
        print_1_slowly("You are being redirected to the Main Menu")
        print_4_slowly("." * 50)
        main_menu()


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


def otc_menu():
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

    fill_cart()

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

    fill_cart()

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

    fill_cart()

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

    fill_cart()

#//////////////////////////////////////////////////////////////
#////                                            fill cart ////
#//////////////////////////////////////////////////////////////

def fill_cart():
    print("Enter item id to add to cart: ")
    print()
    print('-' * 50)
    print()
    fill_cart_input = input('Please enter 1 to return to the main menu or 2 to exit: ')
    print()
    print('-' * 50)

    if fill_cart_input == '1':
        main_menu()
    
    elif fill_cart_input == '2':
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
    pre_menu()
