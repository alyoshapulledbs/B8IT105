# -*- coding: utf-8 -*-
"""
Module       : B8IT105 - Programming for Big Data
Assignment   : CA3 - 10 function sequence calculator 
                using map, reduce, filter and generator.
Description  : Seqence calculator class.
                This class works on sequences only.
Student Code : 10541255
Student Name : Alyosha Pulle
"""

from functools import reduce

class SequenceCalculator():
    
    def min(self, values):
        # Get the mimimum value in a sequence.
        return reduce(lambda a, b : a if (a < b) else b, values) 

    def max(self, values):
        # Get the maximum value in a sequence.
        return reduce(lambda a, b : a if (a > b) else b, values) 
    
    def sum(self, values):
        # Get the sum of values in a sequence.
        return reduce(lambda x, y: x + y, values)
    
    def add(self, first, second):
        # Get new sequence which is sum of two sequences.
        return list(map(lambda x, y: x + y, first, second))

    def is_even(self, values):
        # Get the even numbers in a sequence.
        return filter(lambda x: x % 2 == 0, values)

    def greater_than_mean(self, values):
        # Return all values greater than the meanof the values.
        mean = sum(values) / len(values)
        return filter(lambda x: x > mean, values)

    def to_fahrenheit(self, values):
        # Convert celcius values to fahrenheit.
        return [ ((float(9) / 5) * x + 32) for x in values ]
    