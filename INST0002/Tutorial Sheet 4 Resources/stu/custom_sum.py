#!/usr/bin/env python

# Author: Danny Onah
# Date: 27 Jan.23
# Time: 13:20PM GMT

# A program to calculate the sum of two numbers
def add(num1, num2):
    return num1 + num2

# define the main function
def main():
    num1 = int(input('Please enter Number 1: '))
    num2 = int(input('Please enter Number 2: '))


# define function called add()
    result = add(num1, num2)
    print('The sum is: {}'. format(result))

# start the program
main()

