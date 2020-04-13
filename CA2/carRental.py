
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
        
    def get_diesel_cars(self):
        return self.__diesel_cars

    def get_electric_cars(self):
        return self.__electric_cars

    def get_hybrid_cars(self):
        return self.__hybrid_cars

    def get_petrol_cars(self):
        return self.__petrol_cars

    def get_total_cars(self):
        return (self.get_petrol_cars() + self.get_diesel_cars() +
            self.get_electric_cars() + self.get_hybrid_cars()))

    def load_current_stock(self, csv_file_name):
        # Load the initial list of cars from CSV into the car lists.
        pass
    
    def save_current_stock(self, csv_file_name):
        # Save the current state of car rentals to CSV.
        pass

    def check_availability(self, car_type, amount):
        if (car_type == 'd'): 
            amount_available = self.__get_available_cars(self.get_diesel_cars)
        if (car_type == 'e'): 
            amount_available = self.__get_available_cars(self.get_electric_cars)
        if (car_type == 'h'): 
            amount_available = self.__get_available_cars(self.get_hybrid_cars)
        if (car_type == 'p'): 
            amount_available = self.__get_available_cars(self.get_petrol_cars)
        return len(amount_available) >= amount
        
    def rent_cars(self, car_type, amount):
        # Returns a list of the registrations of the rented cars.
        if (car_type == 'd'): 
            cars = self.get_diesel_cars
        if (car_type == 'e'): 
            cars = self.get_electric_cars
        if (car_type == 'h'): 
            cars = self.get_hybrid_cars
        if (car_type == 'p'): 
            cars = self.get_petrol_cars
        return self.__get_car_registrations(cars, amount)
            
    def return_cars(self, car_type, registrations):
        # For registrations set status to not rented
        pass
    
    def __get_available_cars(cars):
        return filter(lambda x: not x.get_is_rented(), cars)
    
    def __get_car_registrations(self, cars, quantity):
        pass
    