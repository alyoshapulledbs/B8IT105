
"""
Module       : B8IT105 - Programming for Big Data
Assignment   : CA2 - DBS Car Rental application.
Description  : Main script and the Car Rental application class.
Student Code : 10541255
Student Name : Alyosha Pulle
"""

from carRental import CarRental

class CarRentalApp():

    def __init__(self):
        self.__car_rental = CarRental()
    
    def __show_banner(self):
        # Display the application banner.
        print('#'*30)
        print('Welcome to DBS Car Rental')
        print('#'*30, '\n')

    def __show_main_options(self):
        # Show the first level user options
        print('Select from the following options ...')
        option_format = '\t{}\t{}'         
        print(option_format.format(1, 'Rent'))
        print(option_format.format(2, 'Return'))
        print(option_format.format('q', 'Quit'))

    def __show_car_type_options(self):
        # Show the options of car types for selection.
        print('Select from the following options ...')
        option_format = '\t{}\t{}'         
        print(option_format.format('d', 'Diesel'))
        print(option_format.format('e', 'Electric'))
        print(option_format.format('h', 'Hybrid'))
        print(option_format.format('p', 'Petrol'))
        print(option_format.format('q', 'Quit'))

    def __get_user_options(self, valid_options):
        # Validate user input is from a allowed set of characters.
        input_invalid = True
        valid_options = list(valid_options)
        while input_invalid:
            user_input = input('Enter your option: ').lower()
            if user_input in valid_options:
                input_invalid = False
            else:
                print("'{}' is not a valid option.".format(user_input))
        return user_input

    def __get_cars_amount(self, car_type):
        # Get from user how many cars are rented. 
        rentable_amount = self.__car_rental.get_rentable_amount_by_type(car_type)
        print ('The # of cars available for rent - {}'.format(
               rentable_amount))
        input_invalid = True
        while input_invalid:
            amount = input('Please enter a number for the amount or 0 to quit: ')
            if amount.isdigit():
                amount = int(amount)
                if rentable_amount < amount:
                    print('There are not enough cars to rent.' )
                else:
                    input_invalid = False
            else:
                print("'{}' is not a valid amount.".format(amount))
        return amount

    def __show_registrations(self, registrations):
        # Show the list of rented/returned cars.
        for reg in registrations:
            print('\t{}'.format(reg))

    def __do_renting(self):
        # Manages the rental process.
        print('Which type of cars do you want to rent?')
        self.__show_car_type_options()
        car_type = self.__get_user_options('dehpq')
        if car_type == 'q':
            return
        else:
            amount = self.__get_cars_amount(car_type)
            if amount == 0:
                return
            else:
                registrations = self.__car_rental.rent_cars(car_type, amount)
                print('The following cars have been rented.')
                self.__show_registrations(registrations)

    def __get_return_registrations(self, car_type):
        # Gets the registrations of returned cars from the user.
        # Registrations are checked for validity on input.
        print('Please enter the returned car registrations.')
        print('\tEnter d when Done or q to Quit.')
        registrations = []
        get_registrations = True
        while get_registrations == True:
            registration = input('Car registration: ')
            if registration.lower() == 'q':
                registrations.clear()
                get_registrations = False
            elif registration.lower() == 'd':
                get_registrations = False
            elif self.__car_rental.is_rented_car_registration(car_type, registration):
                registrations.append(registration)
            else:
                print("'{}' is not a valid car registration.".format(registration))
        return registrations

    def __do_returns(self):
        # Manages the returns process.
        print('Which type of cars do you want to return?')
        self.__show_car_type_options()
        car_type = self.__get_user_options('dehpq')
        if car_type == 'q':
            return
        else:
            registrations = self.__get_return_registrations(car_type)
            if len(registrations) > 0:
                self.__car_rental.return_validated_cars(car_type, registrations)
                print('The following cars have been returned.')
                self.__show_registrations(registrations)
        
    def __run_user_interface(self):
        # Run the inteeractive application.
        self.__show_banner()
        keep_running = True
        while keep_running:
            self.__show_main_options()
            option = self.__get_user_options('12q')
            if option == '1':
                self.__do_renting()
            elif option == '2':
                self.__do_returns()
            else:
                keep_running = False
        print('Sorry to see you leave. Goodbye.')

    def run_application(self):
        # Loads the CarRental class and on completion of application run
        # saves current status of stock back to the CSV file.
        csv_file_name = 'CarRentalStock.csv'
        self.__car_rental.load_current_stock(csv_file_name)
        self.__run_user_interface()
        self.__car_rental.save_current_stock(csv_file_name)


def main():
    car_rental_app = CarRentalApp()
    car_rental_app.run_application()

if __name__ == "__main__":
    main()









