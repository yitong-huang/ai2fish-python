#!/usr/bin/env python

# Author: Danny Onah
# Date: 27 Jan.23
# Time: 17:40PM GMT
"""
A program that would print out the character with the smallest integer value of their ASCII representation.
"""
def xx(c1, c2, c3):
    int_val1 = ord(c1)
    int_val2 = ord(c2)
    int_val3 = ord(c3)

    print(f"The integer value of '{c1}' is: {int_val1}")
    print(f"The integer value of '{c2}' is: {int_val2}")
    print(f"The integer value of '{c3}' is: {int_val3}")

    smallest_val = min(int_val1, int_val2, int_val3)
    smallest_char = chr(smallest_val)
    return smallest_char # 'a'


# define the main() function
def main():
    char1 = input('Please enter Character 1: ')
    char2 = input('Please enter Character 2: ')
    char3 = input('Please enter Character 3: ')

# define a function findSmallerIntChar() that will take the characters as parameters 
    # result = find_smallest_char(char1, char2, char3)

    result = xx(char1, char2, char3)

    print('The character with the smallest integer value is: {}'. format(result))


# start the program
main()
#
# print(ord('a'))
# print(chr(97))


