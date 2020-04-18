
"""
Module       : B8IT105 - Programming for Big Data
Assignment   : CA2 - DBS Car Rental application.
Description  : Main script for the Car Rental application.
Student Code : 10541255
Student Name : Alyosha Pulle
"""

from carRental import CarRental

def show_banner():
    # Display the application banner.
    print('#'*30)
    print('Welcome to DBS Car Rental')
    print('#'*30, '\n')

def show_main_options():
    # Show the first level user options
    print('Select from the following options ...')
    option_format = '\t{}\t{}'         
    print(option_format.format(1, 'Rent'))
    print(option_format.format(2, 'Return'))
    print(option_format.format('q', 'Quit'))

def show_car_type_options():
    # Show the options of car types for selection.
    print('Select from the following options ...')
    option_format = '\t{}\t{}'         
    print(option_format.format('d', 'Diesel'))
    print(option_format.format('e', 'Electric'))
    print(option_format.format('h', 'Hybrid'))
    print(option_format.format('p', 'Petrol'))
    print(option_format.format('q', 'Quit'))

def get_user_options(valid_options):
    # Validate user input is from a allowed set of characters.
    input_invalid = True
    while input_invalid:
        user_input = input('Enter your option: ').lower()
        if user_input in valid_options:
            input_invalid = False
        else:
            print("'{}' is not a valid option.".format(user_input))
    return user_input

def get_cars_amount(car_type, car_rental):
    # Get from user how many cars are rented. 
    rentable_amount = car_rental.get_rentable_amount_by_type(car_type)
    print ('There are {} cars available for rent.'.format(rentable_amount))
    input_invalid = True
    while input_invalid:
        amount = input('Please enter a number for the amount or 0 to quit: ')
        if amount.isdigit():
            amount = int(amount)
            if rentable_amount < amount:
                print('There are not enough cars to rent.\n' )
            else:
                input_invalid = False
        else:
            print("'{}' is not a valid amount.".format(amount))
    return amount

def do_renting(car_rental):
    print('Which type of cars do you want to rent?')
    show_car_type_options()
    car_type = get_user_options('dehpq')
    if car_type == 'q':
        return
    else:
        amount = get_cars_amount(car_type, car_rental)
        if amount == 0:
            return
        else:
            registrations = car_rental.rent_cars(car_type, amount)
            print('The following cars have been rented.')
            for reg in registrations:
                print('\t{}'.format(reg))

def get_return_registrations(car_rental, car_type):
    print('Please enter the returned car registrations.')
    print('\tEnter d when Done or q to Quit.')
    registrations = []
    get_registrations = True
    while get_registrations == True:
        registration = input('Car registration: ').lower()
        if registration == 'q':
            return []
        elif registration == 'd':
            return registrations
        elif car_rental.is_valid_rented_car_registration(
                car_type, registration):
            registrations.append(registration)
        else:
            print("'{}' is not a valid car registration.".format(registration))

def do_returns(car_rental):
    print('Which type of cars do you want to return?')
    show_car_type_options()
    car_type = get_user_options('dehpq')
    if car_type == 'q':
        return
    else:
        registrations = get_return_registrations(car_rental, car_type)
        if len(registrations) > 0:
            car_rental.return_validated_cars(car_type, registrations)
            print('The following cars have been returned.')
            for reg in registrations:
                print('\t{}'.format(reg))
        
def run_application(car_rental):
    '''
    If returning: get the car type and registrations and update the stock
        Show error message if cannot find the registrations.
    '''
    show_banner()
    keep_running = True
    while keep_running:
        show_main_options()
        option = get_user_options('12q')
        if option == '1':
            do_renting(car_rental)
        elif option == '2':
            do_returns(car_rental)
        else:
            keep_running = False
    print('Sorry to see you leave. Goodbye.')

def main():
    # Loads the CarRental class and on completion of application run
    # saves current status of stock back to the CSV file.
    car_rental = CarRental()
    csv_file_name = 'CarRentalStock.csv'
    car_rental.load_current_stock(csv_file_name)
    run_application(car_rental)
    car_rental.save_current_stock(csv_file_name)

if __name__ == "__main__":
    main()









