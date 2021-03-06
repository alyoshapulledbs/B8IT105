# -*- coding: utf-8 -*-
"""
Module       : B8IT105 - Programming for Big Data
Assignment   : CA3 - 10 function sequence calculator 
                using map, reduce, filter and generator.
Description  : Main script and the sequence calculator application class.
Student Code : 10541255
Student Name : Alyosha Pulle
"""

from SequenceCalculator import SequenceCalculator

class SequenceCalculatorApp():
    # Wrapper class for calculator to handle UI interactions.
    
    def __init__(self):
        self.__calc = SequenceCalculator()
    
    def __show_banner(self):
        # Display the application banner.
        print('#'*52)
        print('Welcome to the sequence calculator with 10 functions')
        print('#'*52, '\n')

    def __show_operands(self):
        # Display the list of functions in the calculator for selection.
        print('Please select the operand from list below or q to Quit.')
        print('\t1 - Minimum value in sequence')
        print('\t2 - Maximum value in sequence')
        print('\t3 - Sum values in sequence')
        print('\t4 - Cube values in sequence')
        print('\t5 - Add two sequences')
        print('\t6 - Even values only in sequence')
        print('\t7 - Values greater than mean in sequence')
        print('\t8 - Convert Celcius values in sequence to Fahrenheit')
        print('\t9 - Get generator of Fibonacci values in given range')
        print('\t0 - Get generator of prime numbers in given range')

    def __get_sequence(self,
                     prompt = 'Please enter the sequence of numbers.', 
                     length = 0):
        # Get a sequence of numbers from the user.
        # If length is specified, user can only create a sequence where the 
        #   number of elements is equal to length.
        print(prompt)
        print('Enter q to Quit or d when Done.')
        value = ''
        sequence = []
        while value not in ['d','q']:
            value = input('Enter number: ').lower()
            if self.__is_number(value):
                sequence.append(float(value))
                print('Sequence ({}) - '.format(len(sequence)), sequence)
                if len(sequence) == length:
                    value = 'd'
            elif value not in ['d','q']:
                print('"{}" is not a valid number.'.format(value))
            elif length > 0 and value == 'd':
                print('Please enter more elements. Require {} more.'
                      .format(length - len(sequence)))
                value = ''
        return sequence if value == 'd' else []

    def __is_number(self, string_to_validate):
        # Validate whether string parameter is a valid number.
        try:
            float(string_to_validate)
            return True
        except:
            return False

    def __get_operand(self):
        # Get the operand from user and allow only valid options.
        self.__show_operands()
        input_not_valid = True 
        while input_not_valid:
            operand = input('Enter option: ').lower()
            if (len(operand) == 1 and
                (operand == 'q' or ('0' <= operand <= '9') )):
                input_not_valid = False
            else:
                print('"{}" is not a valid option.'.format(operand))
        return operand

    def __do_unary_operation(self, operand, sequence):
        # Run the unary functions of the calculator.
        if operand == '1':
            print("The minimum value in sequence {0} is {1}."
                  .format(sequence, self.__calc.min(sequence)))
        elif operand == '2':
            print("The maximum value in sequence {0} is {1}."
                  .format(sequence, self.__calc.max(sequence)))
        elif operand == '3':
            print("The sum of values in sequence {0} is {1}."
                  .format(sequence, self.__calc.sum(sequence)))
        elif operand == '4':
            print("The cube of values in sequence {0} is {1}."
                  .format(sequence, self.__calc.cube(sequence)))
        elif operand == '6':
            print("The even numbers in sequence {0} are {1}."
                  .format(sequence, list(self.__calc.is_even(sequence))))
        elif operand == '7':
            print("The values greater than mean in sequence {0} are {1}."
                  .format(sequence, list(self.__calc.greater_than_mean(sequence))))
        elif operand == '8':
            print("The Fahrenheit of Celcius values in sequence {0} are {1}."
                  .format(sequence, self.__calc.to_fahrenheit(sequence)))

    def __do_add_operation(self):
        # Gets two sequences of same length from the user and does the 
        #   calculator function of adding two sequences.
        sequence1 = self.__get_sequence('Please enter the 1st sequence of numbers.')
        if len(sequence1) == 0: 
            return
        sequence2 = self.__get_sequence('Please enter the 2nd sequence of numbers.',
                                 len(sequence1))
        if len(sequence2) != 0: 
            print('The addition of sequences {0} and {1} is sequence {2}.'
                  .format(sequence1, sequence2, 
                          self.__calc.add(sequence1, sequence2)))

    def __get_integer(self, prompt):
        # Gets input from user and validates whether the input is a positive
        #   integer value.
        input_not_integer = True
        while input_not_integer:
            value = input(prompt)
            if value.isdigit():
                input_not_integer = False
            else:
                print('"{}" is not a valid value.'.format(value))
        return int(value)

    def __get_integer_range(self):
        # Gets integer range from user and validates whether the lower is 
        #   not more than the upper bound.
        range_not_valid = True
        while range_not_valid:
            lower = self.__get_integer('Please enter the positive integer lower bound: ')
            upper = self.__get_integer('Please enter the positive integer upper bound: ')
            if lower > upper:
                print('The input range is not valid.')
            else:
                range_not_valid = False
        return (lower, upper)

    def __do_generators(self, operand):
        # Gets user inputs and runs the calculator functions to get either
        #   the Fibonacci series or primes numbers for the given number range.
        lower, upper = self.__get_integer_range()
        if operand == '9':  
            print("The fibonacci sequence in number range {0} to {1} is {2}."
                  .format(lower, upper, list(self.__calc.fibonacci(lower, upper))))
        else:
            # Prime numbers
            print("The prime numbers in number range {0} to {1} is {2}."
                  .format(lower, upper, list(self.__calc.primes(lower, upper))))
    
    def __get_run_again(self):
        # Check with user whether wish to run another calculation.
        option = ''
        valid_options = ['y', 'n']
        while option not in valid_options:
            option = input('Do you wish to do another calculation? (y/n): ')
            if option not in valid_options:
                print('"{}" is not a valid option.'.format(option))
        return option == 'y'

    def __do_calculation(self):
        # Prompt user and run a single calculation
        operand = self.__get_operand()
        if operand == '5':
            self.__do_add_operation()
        elif operand in ['9','0']:
            self.__do_generators(operand)
        elif operand != 'q':
            sequence = self.__get_sequence()
            if len(sequence) != 0:
                self.__do_unary_operation(operand, sequence)

    def run_application(self):
        # The starting point of the application.
        self.__show_banner()
        keep_running = True
        while keep_running:
            self.__do_calculation()
            keep_running = self.__get_run_again()                
        print('Sorry to see you leave. Goodbye.')

def main():
    SequenceCalculatorApp().run_application()
        
if __name__ == '__main__':
    main()
