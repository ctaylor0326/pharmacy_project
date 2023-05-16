

def create_prescription_table(patient)
    
    # print table header
    # placeholder header columns to be adjusted to match database
    print(f"{'ID':<5}{'Name':<20}{'Quantity':<10}{'Refills':<10}{'Last Refill':<15}{'Expiration':<15}")
    print('-' * 75)

    # print table rows
    for prescription in patient.prescriptions:
        print(f"{prescription.id:<5}{prescription.name:<20}{prescription.quantity:<10}{prescription.refills:<10}{prescription.last_refill:<15}{prescription.expiration:<15}")

def fill_prescription_cart(patient):
    prescription_cart = []
    while True:
        prescription_id = input('Please enter the ID of the prescription you would like to fill, or enter "done" to complete your order: ')
        if prescription_id == 'done':
            break
        prescription = session.query(Prescription).filter(Prescription.id == prescription_id).one_or_none()
        if prescription:
            prescription_cart.append(prescription)
        else:
            print('Invalid ID. Please try again.')
        return prescription_cart
    



greeting_image = """
              _________
             {_________}
              )=======(
             /         \
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
