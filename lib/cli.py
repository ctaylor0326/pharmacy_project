from helpers import *

if __name__ == '__main__':
    print(greeting_image)
    print('Welcome to Walgreenz!')

    # retrieve patient object from the DB

    patient = None
    while not patient:
        store_name = input('Please enter your name: ')
        patient = session.query(Patient).filter(Patient.name == patient_name).one_or_none()

    # display patient info
    print(f'Welcome back, {patient.name}!')
    print(f"Your prescriptions on file are:")

    create_prescription_table(patient)

    # fill prescription cart
    prescription_cart = fill_prescription_cart(patient)

    # display prescription cart
    print('Your prescription cart contains:') 
    create_prescription_table(prescription_cart)

    #remove filled prescriptions from patient's prescriptions
    for prescription in prescription_cart:
        patient.prescriptions.remove(prescription)

    # update prescription table
    create_prescription_table(patient)

    # set prescription pick up time
    print('Thank you for your order! Your prescriptions will be ready for pick up in 15 minutes.')
    print(walgreenz_image)