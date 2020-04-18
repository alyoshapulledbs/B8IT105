
"""
Module       : B8IT105 - Programming for Big Data
Assignment   : CA2 - DBS Car Rental application.
Description  : Class to test the Car Rental application and classes.
Student Code : 10541255
Student Name : Alyosha Pulle
"""

import unittest
from car import Car, DieselCar, ElectricCar, HybridCar, PetrolCar
from carRental import CarRental

class TestCarRentalApp(unittest.TestCase):
    
    def test_car(self):
        car = Car('Volksvagen', 'Passat', 'White', '01 P 1234')
        self.assertEqual(car.get_make(), 'Volksvagen')
        self.assertEqual(car.get_model(), 'Passat')
        self.assertEqual(car.get_colour(), 'White')
        self.assertEqual(car.get_registration(), '01 P 1234')
        self.assertEqual(car.get_is_rented(), False)
        self.assertEqual(str(car), 'Volksvagen,Passat,White,01 P 1234,False')
    
    def test_diesel_car(self):
        car = DieselCar('Volksvagen', 'Passat', 'White', '01 P 1234', 1.5)
        self.assertEqual(car.get_make(), 'Volksvagen')
        self.assertEqual(car.get_model(), 'Passat')
        self.assertEqual(car.get_colour(), 'White')
        self.assertEqual(car.get_registration(), '01 P 1234')
        self.assertEqual(car.get_engine_size(), 1.5)
        self.assertEqual(car.get_is_rented(), False)
        self.assertEqual(str(car), 'Diesel,Volksvagen,Passat,White,01 P 1234,False,1.5,,\n')

    def test_electric_car(self):
        car = ElectricCar('Volksvagen', 'Passat', 'White', '01 P 1234', 2)
        self.assertEqual(car.get_make(), 'Volksvagen')
        self.assertEqual(car.get_model(), 'Passat')
        self.assertEqual(car.get_colour(), 'White')
        self.assertEqual(car.get_registration(), '01 P 1234')
        self.assertEqual(car.get_number_fuel_cells(), 2)
        self.assertEqual(car.get_is_rented(), False)
        self.assertEqual(str(car), 'Electric,Volksvagen,Passat,White,01 P 1234,False,,2,\n')

    def test_hybrid_car(self):
        car = HybridCar('Volksvagen', 'Passat', 'White', '01 P 1234', 1.5,
                        'MHEV')
        self.assertEqual(car.get_make(), 'Volksvagen')
        self.assertEqual(car.get_model(), 'Passat')
        self.assertEqual(car.get_colour(), 'White')
        self.assertEqual(car.get_registration(), '01 P 1234')
        self.assertEqual(car.get_engine_size(), 1.5)
        self.assertEqual(car.get_hybrid_type(), 'MHEV')
        self.assertEqual(car.get_is_rented(), False)
        self.assertEqual(str(car), 'Hybrid,Volksvagen,Passat,White,01 P 1234,False,1.5,,MHEV\n')

    def test_petrol_car(self):
        car = PetrolCar('Volksvagen', 'Passat', 'White', '01 P 1234', 2)
        self.assertEqual(car.get_make(), 'Volksvagen')
        self.assertEqual(car.get_model(), 'Passat')
        self.assertEqual(car.get_colour(), 'White')
        self.assertEqual(car.get_registration(), '01 P 1234')
        self.assertEqual(car.get_engine_size(), 2)
        self.assertEqual(car.get_is_rented(), False)
        self.assertEqual(str(car), 'Petrol,Volksvagen,Passat,White,01 P 1234,False,2,,\n')

    def test_car_rental(self):
        # Load
        car_rental = CarRental()
        car_rental.load_current_stock('test_CarRentalStock.csv')
        self.assertEqual(len(car_rental.get_diesel_cars()), 10)        
        self.assertEqual(len(car_rental.get_electric_cars()), 6)        
        self.assertEqual(len(car_rental.get_hybrid_cars()), 4)        
        self.assertEqual(len(car_rental.get_petrol_cars()), 20)
        # Renting
        car_rental.rent_cars('p', 3)
        rented_cars = len([1 for car in car_rental.get_petrol_cars() 
                if car.get_is_rented() == True])
        self.assertEqual(rented_cars, 3, 
                 'The petrol cars list has not been updated correctly with the # of rented cars.')
        # Returns validation
        self.assertTrue(
                car_rental.is_rented_car_registration('p', '01 P 1002'))        
        self.assertFalse(
                car_rental.is_rented_car_registration('p', '06 G 1002'))
        # Returns
        car_rental.return_validated_cars('p', ['01 P 1002','01 P 1003'])
        rented_cars = len([1 for car in car_rental.get_petrol_cars() 
                            if car.get_is_rented() == True])
        self.assertEqual(rented_cars, 1,
                 'The returned cars have not been updated correctly in the petrol cars list.')

if __name__ == "__main__":
    unittest.main()
