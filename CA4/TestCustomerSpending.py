# -*- coding: utf-8 -*-
"""
Module       : B8IT105 - Programming For Big Data
Assignment   : CA4 - DataFrames using Pandas
Student Code : 10541255
Student Name : Alyosha Pulle
"""

import unittest
from CustomerSpending import CustomerSpending

class TestCustomerSpending(unittest.TestCase):
    # Class for testing the load and clean functions of the CustomerSpending class.
    
    def setUp(self):
        self.cs = CustomerSpending()
        
    def test_data_before_clean(self):
        self.assertEqual((440, 8), self.cs.get_df_spending().shape)
        self.assertEqual(0, self.cs.nan_count())
        
    def test_data_after_clean(self):
        self.cs.clean_data()
        self.assertEqual('Delicatessen', self.cs.get_df_spending().columns[-2])
        self.assertEqual('Total', self.cs.get_df_spending().columns[-1])
    
if __name__ == '__main__':
    unittest.main()

