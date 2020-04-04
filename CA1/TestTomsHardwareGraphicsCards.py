
"""
Module       : B8IT105 - Programming for Big Data
Assignment   : CA1 - Scrape website graphics cards to CSV.
Description  : Unit tests for class to scrape website graphic cards.
Student Code : 10541255
Student Name : Alyosha Pulle
"""

import unittest
from TomsHardwareGraphicsCards import TomsHardwareGraphicsCards

class TestTomsHardwareGraphicsCards(unittest.TestCase):
    def setUp(self):
        self.__cards = TomsHardwareGraphicsCards()
    
    def test_table_contents(self):
        self.assertEqual(len(self.__cards.get_table_column_headers()), 
                 7, 'The number of table column headers have changed from 7.')
        self.assertGreaterEqual(len(self.__cards.get_table_rows()), 
                1, 'There are no rows in the table.')

if __name__ == '__main__':
    unittest.main()
