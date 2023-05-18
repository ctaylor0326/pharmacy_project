from helpers import *
from db.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import click
from tabulate import tabulate
import time

engine = create_engine('sqlite:///pharmacy.db')
Session = sessionmaker(bind=engine)
session = Session()

#/////////////////////////////////////////////////////////
#////                      style and formatting functions
#/////////////////////////////////////////////////////////


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


#/////////////////////////////////////////////////////////
#////                        navication and menu functions
#/////////////////////////////////////////////////////////

def pre_menu():
        click.clear()
        print()
        print('-' * 50)
        print(walgreenz_image)
        print_1_slowly(greeting_image)
        print()
        print_4_slowly('Welcome to Walgreenz!')
        print_8_slowly('Welc o m e  t o  W a l g r e e n z !')
        print_16_slowly('W e l c o  m  e   t  o   W  a  l  g  r  e  e  n  z  !')
        print('-' * 50)
        main_menu()
    
def main_menu():
        click.clear()
        print_1_slowly(main_menu_image)       
        print('-' * 50)
        print()
        print()
        print_8_slowly("1.|   L o g i n / S i g n   U p")
        print_8_slowly("2.|   O v e r   t h e   C o u n t e r")
        print_8_slowly("3.|   S h o p p i n g   C a r t")
        print_16_slowly("4.|   E X I T")
        print('-' * 50)
        input("Please enter a number from the menu above: ")
        print('-' * 50)

        if input == '1':
            login()

        elif input == '2':
             otc()

        elif input == '3':
            shopping_cart()

        elif input == '4':
            print(walgreenz_image)
            print_max_slowly('T h a n k   y o u   f o r   c h o o s i n g   W a l g r e e n z !')
            exit()

        else:
            print('Invalid choice. Please try again.')



def login():
        click.clear()
        print_1_slowly(login_image)
        print('-' * 50)
        print()
        print()
        input('Please  enter  your  LOGIN: ')
        input('Please enter your PASSWORD: ')
        # while not patient:
            # patient_id = input('Please enter your patient ID: ')
            # patient = session.query(Patient).filter(Patient.id == patient_id).one_or_none()
        print()
        # user_greeting(patient)
        user_greeting()


# def user_greeting(patient):
def user_greeting():
        click.clear()
        print_1_slowly(welcome_back_image)
        print()
        print('-' * 50)
        print()
        # print_slowly(f'Welcome back, {patient.first_name} {patient.last_name}!')
        print_16_slowly(f'Welcome back, John Smith!')
    #retrieve patient prescriptions
        # script_on_file = session.query(Prescription).filter(Prescription.patient_id == patient.id).one_or_none()
        print_16_slowly("Would you like to see your prescriptions?")
        print()
        print('-' * 50)
        print()
        first_menu_input = input('Please enter 1 for yes or 2 for no: ')
        print()
        print('-' * 50)

        if first_menu_input == '1':
            # first_menu_input_yes(script_on_file)
            first_menu_input_yes()

        elif first_menu_input == '2':
            print_16_slowly('Thank you for choosing Walgreenz!')
            print(walgreenz_image)
            main_menu()

        else:
            print('-' * 50)
            print()
            print('Invalid choice. Please try again.')
            print()
            print('-' * 50)


# def first_menu_input_yes(script_on_file):
def first_menu_input_yes():
        click.clear()
        print_1_slowly(prescriptions_image)
        # medication = session.query(Medication).filter(Medication.id == script_on_file.prescription_id).one_or_none()
        # print(f'{medication.name} {medication.dosage} {medication.quantity} {medication.price}')
        print_8_slowly(f'1.|   Lipitor   |   20mg   |   30   |   $10.00   |')
        print()
        print()
        # print(f'Would you like to fill your prescription for {medication.name}?')
        print_8_slowly('Would you like to fill your prescription for Lipitor?')
        print()
        print('-' * 50)
        # input_rx_menu('Please enter 1 for yes or 2 for no: ')
        # input_exit_menu('Please enter 1 to return to the main menu or 2 to exit: ')

        second_menu_input = input()
        if second_menu_input == '1':
            # second_menu_input_yes(medication)
            second_menu_input_yes()

        elif second_menu_input == '2':
            print('Your prescription will not be filled.')
            print_8_slowly('Thank you for choosing Walgreenz!')
            print()
            print('-' * 50)
            print()
            print(walgreenz_image)
            main_menu()

        else:
            print('Invalid choice. Please try again.')


# def second_menu_input_yes(medication):
def second_menu_input_yes():
        # print(f'Your {medication.name} prescriptions will be ready for pick up in 15 minutes.')
        print('Your Lipitor prescriptions will be ready for pick up in 45 minutes.')
        print_8_slowly('Thank you for choosing Walgreenz!')
        print(walgreenz_image)
        main_menu()


#/////////////////////////////////////////////////////////////
#////                                    Welcome to Walgreenz!
#/////////////////////////////////////////////////////////////


if __name__ == '__main__':
    pre_menu()