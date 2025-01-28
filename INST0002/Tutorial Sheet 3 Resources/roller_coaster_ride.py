 #!/usr/bin/env python
"""
A Roller coaster ride program.
"""
# Author: Danny Onah
# Date: 20 Jan.2023
# Time: 15:12PM GMT

import random
# define a sentinel value to use
SENTINEL = -999
# this will produce random numbers from 1 - 100 limit


# use a while loop


# define the try and except block here
while True:
    name = input("Please enter your name: ")
    if name == '' or name == 'n':
        break
    try:
        # declare the conditional statement to check for the first condition
        age = int(input("Please enter your age: "))
        # declare the conditional statement to check whether the customer is under-age
    except ValueError:
        # display the results of the exception
        print("Please enter age as integers-whole numbers only...")
        continue

    if age == SENTINEL:
        break
    elif age >= 18:
        secretNumber = random.randint(1, 100)
        print("Welcome {} , Ride number is: {}".format(name, secretNumber))
    else:
        print("You are a junior, therefore you are not authorised to book the roller coaster ride!")

print("Thank you for coming. See you again!")