#!/usr/bin/env python

# Author: Danny Onah
# Date: 27 Jan.23
# Time: 17:46PM GMT
"""
A program to calculate function overloaded and boolean values
"""

# define the main() function
def main():
    number1 = int(input("Please enter Number 1: "))
    number2 = int(input("Please enter Number 2: "))
    bool1 = input("Please enter boolean 1 (True/False): ").strip().lower() == 'true'
    bool2 = input("Please enter boolean 2 (True/False): ").strip().lower() == 'true'

    int_result = sum_number_int(number1, number2)
    float_result = sum_number_float(float(number1), float(number2))  # Converting integers to floats
    bool_result = add_boolean(bool1, bool2)

    print(f"- - -> add({number1}, {number2}) - - - > returns {int_result}")
    print(f"- - -> add({float(number1)}, {float(number2)}) - - - > returns {float_result}")
    print(f"- - -> add({bool1}, {bool2}) - - - > returns {bool_result}")

# define a function sum_number() for the integer numbers
def sum_number(a: int, b: int):
    """Adds two integers and returns the sum."""
    return a + b


# define another sum_number() for the floating-point numbers 
def sum_number(a: float, b: float):
    """Adds two floating-point numbers and returns the sum."""
    return a + b


# define a function add() for the boolean inputs
def sum_number(a: bool, b: bool):
    """Performs logical OR (similar to adding boolean values as 1 + 1 = 1)."""
    return bool1 or bool2

# start the program
main()

