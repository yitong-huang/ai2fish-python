#!/usr/bin/env python

# Author: Danny Onah
# Date: 17 Feb.23
# Time: 14:11PM GMT

"""
A program to compute the average of numbers using lists
"""

def average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return "Cannot calculate average of an empty list."

def main():
    while True:
        try:
            length = input("Enter the length of the list: ")
            if not length.strip():
                raise ValueError("Invalid entry! Please enter integer ONLY.")
            length = int(length)
            if length <= 0:
                raise ValueError("Please enter positive integer ONLY!")
            break
        except ValueError as e:
            print(e)

    numbers = []
    for i in range(length):
        while True:
            try:
                num = input(f"Enter a number for index {i}: ")
                if num.lower() == "done":
                    if len(numbers) == 0:
                        raise ValueError("Invalid entry! Please enter integer ONLY.")
                    print(f"\nThe average is: {average(numbers):.2f}")
                    print(numbers)
                    return
                numbers.append(int(num))
                break
            except ValueError:
                print("Invalid entry! Please enter integer ONLY.")

    print(f"The average is: {average(numbers):.2f}")
    print(numbers)

main()

# create the body of your program here


# define the function average()

	# define the looping construct
	# this for-loop take control of the size of the list
		

	# take user input here

	# check condition if number is equal to 'done'

	# compute the average to 2 decimal points

		
