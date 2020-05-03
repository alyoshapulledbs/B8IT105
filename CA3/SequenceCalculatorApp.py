# -*- coding: utf-8 -*-
"""
Module       : B8IT105 - Programming for Big Data
Assignment   : CA3 - 10 function sequence calculator 
                using map, reduce, filter and generator.
Description  : Main script for the sequence calculator application.
Student Code : 10541255
Student Name : Alyosha Pulle
"""

from SequenceCalculator import SequenceCalculator

def show_banner():
    # Display the application banner.
    print('#'*52)
    print('Welcome to the sequence calculator with 10 functions')
    print('#'*52, '\n')

def show_operands():
    # Display the list of functions in the calculator for selection.
    print('Please select the operand from list below or q to Quit.')
    print('\t1 - Minimum value')
    print('\t2 - Maximum value')
    print('\t3 - Sum values')
    print('\t4 - Add sequences')
    print('\t5 - Even values only')
    print('\t6 - Values greater than mean')
    print('\t7 - Convert to Fahrenheit')
    print('\t8 - ')
    print('\t9 - ')
    print('\t0 - ')

def get_sequence():
    # Get a sequence of numbers from the user.
    print('Please enter the sequence of numbers.')
    print('Enter q to Quit or d when Done.')
    value = ''
    sequence = []
    while value not in ['d','q']:
        value = input('Enter number: ').lower()
        if is_number(value):
            sequence.append(float(value))
            print('Sequence ({}) - '.format(len(sequence)), sequence)
        elif value not in ['d','q']:
            print('"{}" is not a valid number.'.format(value))
    return sequence if value == 'd' else []

def is_number(string_to_validate):
    # Validate whether string parameter is a valid number.
    try:
        float(string_to_validate)
        return True
    except:
        return False

def get_operand():
    # Get the operand from user and allow only valid options.
    show_operands()
    input_not_valid = True 
    while input_not_valid:
        operand = input('Enter option: ').lower()
        if (len(operand) == 1 and
            (operand == 'q' or ('0' <= operand <= '9') )):
            input_not_valid = False
        else:
            print('"{}" is not a valid option.'.format(operand))
    return operand

def do_unary_operation(sequence, operand):
    # Run the unary functions of the calculator.
    calc = SequenceCalculator()
    if operand == '1':
        print("The minimum value in sequence {0} is {1}."
              .format(sequence, calc.min(sequence)))
    elif operand == '2':
        print("The maximum value in sequence {0} is {1}."
              .format(sequence, calc.max(sequence)))
    elif operand == '3':
        print("The sum of values in sequence {0} is {1}."
              .format(sequence, calc.sum(sequence)))
    elif operand == '5':
        print("The even numbers in sequence {0} are {1}."
              .format(sequence, calc.is_even(sequence)))
    elif operand == '6':
        print("The values greater than mean in sequence {0} are {1}."
              .format(sequence, calc.greater_than_mean(sequence)))
    elif operand == '7':
        print("The fahrenheit of values in sequence {0} are {1}."
              .format(sequence, calc.to_fahrenheit(sequence)))

def get_run_again():
    # Check with user whether wish to run another calculation.
    option = ''
    valid_options = ['y', 'n']
    while option not in valid_options:
        option = input('Do you wish to do another calculation? (y/n): ')
        if option not in valid_options:
            print('"{}" is not a valid option.'.format(option))
    return option == 'y'

def do_calculation():
    # Prompt user and run a single calculation
    sequence = get_sequence()
    if len(sequence) > 0:
        operand = get_operand()
        if operand == '4':
            sequence2 = get_sequence()
            # Do calculation
        elif operand != 'q':
            do_unary_operation(sequence, operand)

def main():
    # The starting point of the application.
    show_banner()
    keep_running = True
    while keep_running:
        do_calculation()
        keep_running = get_run_again()                
    print('Sorry to see you leave. Goodbye.')
        
if __name__ == '__main__':
    main()
