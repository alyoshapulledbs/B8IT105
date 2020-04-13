
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

def show_renting_car_options():
    # Show the options of car types.
    print('Which type of car do you want to rent?')
    print('Select from the following options ...')
    option_format = '\t{}\t{}'         
    print(option_format.format('d', 'Diesel'))
    print(option_format.format('e', 'Electric'))
    print(option_format.format('h', 'Hybrid'))
    print(option_format.format('p', 'Petrol'))
    print(option_format.format('q', 'Quit'))

def get_user_options(valid_options):
    # Shared function to validate user input is from a allowed set of
    # characters.
    input_invalid = True
    while input_invalid:
        user_input = input('Enter your option: ').lower()
        if user_input in valid_options:
            input_invalid = False
        else:
            print("'{}' is not a valid option.".format(user_input))
    return user_input

def get_cars_amount(car_type):
        

def do_renting():
    show_renting_car_options()
    option = get_user_options('dehpq')
    if option == 'q':
        return
    else:
        get_cars_amount(option)

def do returns():
    pass

def run_application():
    '''
    If renting; check stock and either show not enough cars or list registrations.
    If returning: get the car type and registrations and update the stock
        Show error message if cannot find the registrations.
    '''
    show_banner()
    keep_running = True
    while keep_running:
        show_main_options()
        option = get_user_options('12q')
        if option == '1':
            do_renting()
        if option == '2':
            do_returns()
        else:
            keep_running = False

main():
    car_rental = CarRental()
    csv_file_name = 'CarRentalStock.csv'
    car_rental.load_current_stock(csv_file_name)
    run_application(car_rental)
    car_rental.save_current_stock(csv_file_name)

if __name__ == "__main__":
    main()
