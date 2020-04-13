
"""
Module       : B8IT105 - Programming for Big Data
Assignment   : CA2 - DBS Car Rental application.
Description  : Class to test the Car Rental application and classes.
Student Code : 10541255
Student Name : Alyosha Pulle
"""

import unittest
from car import Car, DieselCar, ElectricCar, HybridCar, PetrolCar

class TestCarRentalApp(unittest.TestCase):

    def test_car(self):
        car = Car('Volksvagen', 'Passat', 'White', '01P1234')
        self.assertEqual(car.get_make(), 'Volksvagen')
        self.assertEqual(car.get_model(), 'Passat')
        self.assertEqual(car.get_colour(), 'White')
        self.assertEqual(car.get_registration(), '01P1234')
        self.assertEqual(car.get_is_rented(), False)
    
    def test_diesel_car(self):
        car = DieselCar('Volksvagen', 'Passat', 'White', '01P1234', '2L')
        self.assertEqual(car.get_make(), 'Volksvagen')
        self.assertEqual(car.get_model(), 'Passat')
        self.assertEqual(car.get_colour(), 'White')
        self.assertEqual(car.get_registration(), '01P1234')
        self.assertEqual(car.get_engine_size(), '2L')
        self.assertEqual(car.get_is_rented(), False)

    def test_electric_car(self):
        car = ElectricCar('Volksvagen', 'Passat', 'White', '01P1234', 2)
        self.assertEqual(car.get_make(), 'Volksvagen')
        self.assertEqual(car.get_model(), 'Passat')
        self.assertEqual(car.get_colour(), 'White')
        self.assertEqual(car.get_registration(), '01P1234')
        self.assertEqual(car.get_number_fuel_cells(), 2)
        self.assertEqual(car.get_is_rented(), False)

    def test_hybrid_car(self):
        car = HybridCar('Volksvagen', 'Passat', 'White', '01P1234', '2L',
                        'MHEV')
        self.assertEqual(car.get_make(), 'Volksvagen')
        self.assertEqual(car.get_model(), 'Passat')
        self.assertEqual(car.get_colour(), 'White')
        self.assertEqual(car.get_registration(), '01P1234')
        self.assertEqual(car.get_engine_size(), '2L')
        self.assertEqual(car.get_hybrid_type(), 'MHEV')
        self.assertEqual(car.get_is_rented(), False)

    def test_petrol_car(self):
        car = PetrolCar('Volksvagen', 'Passat', 'White', '01P1234', '2L')
        self.assertEqual(car.get_make(), 'Volksvagen')
        self.assertEqual(car.get_model(), 'Passat')
        self.assertEqual(car.get_colour(), 'White')
        self.assertEqual(car.get_registration(), '01P1234')
        self.assertEqual(car.get_engine_size(), '2L')
        self.assertEqual(car.get_is_rented(), False)

    def test_car_rental():
        pass
        
if __name__ == "__main__":
    unittest.main()
