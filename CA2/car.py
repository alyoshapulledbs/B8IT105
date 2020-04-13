
"""
Module       : B8IT105 - Programming for Big Data
Assignment   : CA2 - DBS Car Rental application.
Description  : Contains the Car class and subclass definitions.
                Subclasses are ElectricCar, PetrolCar, DieselCar, HybridCar.
Student Code : 10541255
Student Name : Alyosha Pulle
"""

class Car():
    # The base class definition for a car.
    def __init__(self, make, model, colour, registration):
        # Initialise the properties on creation
        self.__make = make
        self.__model = model
        self.__colour = colour
        self.__registration = registration
        self.__is_rented = False

    # Accessors
        
    def get_make(self): 
        return self.__make;

    def get_model(self): 
        return self.__model;
    
    def get_colour(self): 
        return self.__colour;
    
    def get_registration(self): 
        return self.__registration;

    def get_is_rented(self):
        return self.__is_rented

    def set_is_rented(self, value):
        self.__is_rented = value

### Subclasses

class ElectricCar(Car):
    # The class definition for an electric car.
    def __init__(self, make, model, colour, registration, number_fuel_cells):
        # Initialise the properties on creation
        Car.__init__(make, model, colour, registration)
        self.__number_fuel_cells = number_fuel_cells
    
    def get_number_fuel_cells(self):
        return self.__number_fuel_cells

   
class DieselCar(Car):
    # The class definition for a diesel car.
    def __init__(self, make, model, colour, registration, engine_size):
        # Initialise the properties on creation
        Car.__init__(make, model, colour, registration)
        self.__engine_size = engine_size

    def get_engine_size(self):
        return self.__engine_size


class HybridCar(Car):
    # The class definition for a hybrid car.
    def __init__(self, make, model, colour, registration, engine_size,
                 hybrid_type):
        # Initialise the properties on creation
        Car.__init__(make, model, colour, registration)
        self.__engine_size = engine_size
        self.__hybrid_type = hybrid_type

    def get_engine_size(self):
        return self.__engine_size

    def get_hybrid_type(self):
        return self.__hybrid_type


class PetrolCar(Car):
    # The class definition for a petrol car.
    def __init__(self, make, model, colour, registration, engine_size):
        # Initialise the properties on creation
        Car.__init__(make, model, colour, registration)
        self.__engine_size = engine_size

    def get_engine_size(self):
        return self.__engine_size
