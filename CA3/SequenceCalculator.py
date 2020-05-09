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

    def cube(self, values):
        # Get new sequence which is the cube of values in a sequence.
        return list(map(lambda x: x ** 3, values))
    
    def add(self, first, second):
        # Get new sequence which is sum of two sequences.
        return list(map(lambda x, y: x + y, first, second))

    def is_even(self, values):
        # Get the even numbers in a sequence.
        return filter(lambda x: x % 2 == 0, values)

    def greater_than_mean(self, values):
        # Return all values greater than the mean of the values.
        mean = sum(values) / len(values)
        return filter(lambda x: x > mean, values)

    def to_fahrenheit(self, values):
        # Convert celcius values to fahrenheit.
        return [ ((float(9) / 5) * x + 32) for x in values ]
    
    def fibonacci(self, low, high):
        # Get fibonacci sequence in number range low to high.
        n_minus_2 = 0
        if n_minus_2 == low: 
            yield n_minus_2
        n_minus_1 = 1
        if low <= n_minus_1 <= high: 
            yield n_minus_1
        counter = 1
        next_in_series = lambda m, n: m + n
        n = next_in_series(n_minus_2, n_minus_1)
        while n <= high:
            if low <= n: 
                yield n
            n_minus_2 = n_minus_1
            n_minus_1 = n
            counter += 1
            n = next_in_series(n_minus_2, n_minus_1)

    def primes(self, low, high):
        # Get prime numbers in number range low to high.
        for value in range(low, high + 1):
            if value < 2:
                pass
            elif value == 2:
                yield value
            elif value % 2 == 1:
                boundary = value ** .5
                i = 3
                while i <= boundary and value % i != 0:
                    i += 2
                if i > boundary : 
                    yield value
         