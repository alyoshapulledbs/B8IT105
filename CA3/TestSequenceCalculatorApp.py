# -*- coding: utf-8 -*-
"""
Module       : B8IT105 - Programming for Big Data
Assignment   : CA3 - 10 function sequence calculator 
                using map, reduce, filter and generator.
Description  : Unit tests for the sequence calculator application.
Student Code : 10541255
Student Name : Alyosha Pulle
"""

import unittest
from SequenceCalculator import SequenceCalculator

class TestSequenceCalculator(unittest.TestCase):
    
    def setUp(self):
        self.__test_seq1 = [ 9, 20, 4, 11, -7, 18, 13.5 ]
        self.__bad_sequence = self.__test_seq1 + ['a']
        self.__test_seq2 = [ 21, 15.5, 6.0, -9, -13, 2, 6.5 ]
        self.__sequenceCalculator = SequenceCalculator()
    
    def test_min(self):
        # Tests the calculator min() function.
        self.assertEqual(-7, self.__sequenceCalculator.min(self.__test_seq1))
        with self.assertRaises(TypeError):
            self.__sequenceCalculator.min(self.__bad_sequence)
        
    def test_max(self):
        # Tests the calculator max() function.
        self.assertEqual(20, self.__sequenceCalculator.max(self.__test_seq1))
        with self.assertRaises(TypeError):
            self.__sequenceCalculator.max(self.__bad_sequence)

    def test_sum(self):
        # Tests the calculator sum() function.
        self.assertEqual(68.5, self.__sequenceCalculator.sum(self.__test_seq1))
        with self.assertRaises(TypeError):
            self.__sequenceCalculator.sum(self.__bad_sequence)

    def test_add(self):
        # Tests the calculator add() function.
        result = [ 30, 35.5, 10, 2, -20, 20, 20 ]
        self.assertEqual(result, 
                         self.__sequenceCalculator.add(self.__test_seq1,
                                                       self.__test_seq2))
    def test_is_even(self):
        # Tests the calculator is_even() function.
        result = [ 20, 4, 18 ]
        self.assertEqual(result, 
                     list(self.__sequenceCalculator.is_even(self.__test_seq1)))
        with self.assertRaises(TypeError):
            list(self.__sequenceCalculator.is_even(self.__bad_sequence))

    def test_greater_than_mean(self):
        self.assertEqual([ 20, 11, 18, 13.5 ], 
                         list(self.__sequenceCalculator
                              .greater_than_mean(self.__test_seq1)))

    def test_to_fahrenheit(self):
        result = [ 48.2, 68.0, 39.2, 51.8, 19.4, 64.4, 56.3 ]
        self.assertEqual(result, self.__sequenceCalculator
                             .to_fahrenheit(self.__test_seq1))
        
if __name__ == '__main__':
    unittest.main()
