#!/usr/bin/env python

# Author : Danny Onah
# Date : 19/08/2022
# Time : 7.32PM BST

# Create functions for a Game puzzle

# add the functions for the game puzzle according to the task brief


def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

def main():
# take the input using the correct data type
    print("Let's do some math with just functions!")

    age1 = float(input("Enter first age: "))
    age2 = float(input("Enter second age: "))
    age = add(age1, age2)

    height1 = float(input("Enter first height: "))
    height2 = float(input("Enter second height: "))
    height = subtract(height1, height2)

    weight1 = float(input("Enter first weight: "))
    weight2 = float(input("Enter second weight: "))
    weight = multiply(weight1, weight2)

    iq1 = float(input("Enter first iq: "))
    iq2 = float(input("Enter second iq: "))
    iq = divide(iq1, iq2)


    print(f'Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}')
    print('Here is the puzzle.')

# create a puzzle for extra credit, type it anyway or print any message you wish.
    iq_divided = divide(iq, 2)

    weight_multiplied = multiply(weight, iq_divided)

    height_subtracted = subtract(height, weight_multiplied)

    final_result = add(age, height_subtracted)

    print(f'That becomes: {final_result}. Can you do this by hand?')
# convert the formula :-  k = a + (h - (w * iq/2))  to python consrtuct


# display the output
main()

