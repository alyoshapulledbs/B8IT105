
"""
Module       : B8IT105 - Programming for Big Data
Assignment   : CA2 - DBS Car Rental application.
Description  : Contains the CarRental class with methods to load/save current 
                stock, record rentals and returns of cars.
Student Code : 10541255
Student Name : Alyosha Pulle
"""

from car import DieselCar, ElectricCar, HybridCar, PetrolCar

class CarRental():

    def __init__(self):
        self.__diesel_cars = []
        self.__electric_cars = []
        self.__hybrid_cars = []
        self.__petrol_cars = []
        self.__csv_header = ''

    ### Accessors
        
    def get_diesel_cars(self):
        return self.__diesel_cars

    def get_electric_cars(self):
        return self.__electric_cars

    def get_hybrid_cars(self):
        return self.__hybrid_cars

    def get_petrol_cars(self):
        return self.__petrol_cars

#    def get_total_cars(self):
#        return (self.get_petrol_cars() + self.get_diesel_cars() +
#            self.get_electric_cars() + self.get_hybrid_cars())

    ### Actions
    
    def load_current_stock(self, csv_file_name):
        # Load the initial list of cars from CSV into the car lists.
        file = open(csv_file_name, 'r')
        for csv_line in file:
            cols = csv_line.strip().split(',')
            if cols[0] ==  'Diesel':
                self.__load_diesel_car(cols)
            elif cols[0] ==  'Electric':
                self.__load_electric_car(cols)
            elif cols[0] ==  'Hybrid':
                self.__load_hybrid_car(cols)
            elif cols[0] ==  'Petrol':
                self.__load_petrol_car(cols)
            else:
                # Save the header row
                self.__csv_header = csv_line
        file.close()
            
    def save_current_stock(self, csv_file_name):
        # Save the current state of car rentals to CSV.
        file = open(csv_file_name, 'w')
        file.write(self.__csv_header)
        self.__write_cars_csv(file, self.get_diesel_cars())
        self.__write_cars_csv(file, self.get_electric_cars())
        self.__write_cars_csv(file, self.get_hybrid_cars())
        self.__write_cars_csv(file, self.get_petrol_cars())
        file.close()

    def get_rentable_amount_by_type(self, car_type):
        # Get the # of cars available to rent of given car type.
        cars = self.__get_cars_of_type(car_type)
        return len([1 for car in cars if not car.get_is_rented()])
        
    def rent_cars(self, car_type, amount):
        # Returns a list of the registrations of the amount of rented cars.
        cars = (car for car in self.__get_cars_of_type(car_type)
                if not car.get_is_rented())
        return [self.__process_car_rental(next(cars)) for x in range(amount)]
            
    def return_validated_cars(self, car_type, registrations):
        # For returned registrations set status to not rented
        for car in self.__get_cars_of_type(car_type):
            if car.get_registration() in registrations:
                car.set_is_rented(False)

    def is_valid_rented_car_registration(self, car_type, registration):
        # Check whether registration for car type is for valid rented car.
        registrations = [car.get_registration() 
                for car in self.__get_cars_of_type(car_type)
                if car.get_is_rented() == True]
        if registration in registrations:
            return True
        else:
            return False
            
    ### Private functions

    def __write_cars_csv(self, file, cars):
        for car in cars:
            file.write(str(car))

    def __load_diesel_car(self, cols):
        # Create diesel car from CSV line and add to diesel car list.
        car = DieselCar(cols[1], cols[2], cols[3], cols[4], float(cols[6]))
        self.__load_car_rental_status(car, cols[5])
        self.get_diesel_cars().append(car)
    
    def __load_electric_car(self, cols):
        # Create electric car from CSV line and add to electric car list.
        car = ElectricCar(cols[1], cols[2], cols[3], cols[4], int(cols[7]))
        self.__load_car_rental_status(car, cols[5])
        self.get_electric_cars().append(car)
    
    def __load_hybrid_car(self, cols):
        # Create hybrid car from CSV line and add to hybrid car list.
        car = HybridCar(cols[1], cols[2], cols[3], cols[4], float(cols[6]),
                        cols[8])
        self.__load_car_rental_status(car, cols[5])
        self.get_hybrid_cars().append(car)
    
    def __load_petrol_car(self, cols):
        # Create petrol car from CSV line and add to petrol car list.
        car = PetrolCar(cols[1], cols[2], cols[3], cols[4], float(cols[6]))
        self.__load_car_rental_status(car, cols[5])
        self.get_petrol_cars().append(car)
    
    def __load_car_rental_status(self, car, status):
        # Convert rental status in CSV ti boolean
        car.set_is_rented(True if status == 'True' else False)
    
    def __get_cars_of_type(self, car_type):
        # Get the list of cars for car type.
        if (car_type == 'd'): 
            return self.get_diesel_cars()
        if (car_type == 'e'): 
            return self.get_electric_cars()
        if (car_type == 'h'): 
            return self.get_hybrid_cars()
        if (car_type == 'p'): 
            return self.get_petrol_cars()
    
    def __process_car_rental(self, car):
        # Update rental status and retrun registrration.
        car.set_is_rented(True)
        #print(car.get_is_rented(), car.get_registration())
        return car.get_registration()


