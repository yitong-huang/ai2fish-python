#!/usr/bin/env python
# Author: Danny Onah
# Date: 27 Jan.23
# Time: 00:40AM GMT
"""
A program to print a quote
"""

# define the main() function

# use conditional statement to check the input
def main():
    choice = input('Would you like a quote? [y/n]:')
    if choice == 'y' or choice == 'yes':
        printQuote()
    elif choice == 'n' or choice == 'no':
        printComeBackAgain()


# define a function printQuote()
def printQuote():
    print('"Learning never exhausts the mind."')
    print('    – Leonardo da Vinci')


# define a function printComeBackAgain()
def printComeBackAgain():
    print('Come back again!')


# start the program
main()