#!/usr/bin/env python
# Author : Danny Onah
# Date : 20 July 2022
# Time : 11.40AM GMT

"""
A program to demonstrate a pessenger car pool management company
"""


# number of cars
cars = 100 

# number of space in a car
space_in_a_car = 4 

# number of drivers in the car company
drivers = 30 

# number of passengers for the journey
passengers = 90 

#  Compute or calculate the number of cars driven
cars_driven = drivers

#  Compute or calculate the number of cars not driven
cars_not_driven = cars - cars_driven

# Compute or calculate the capcity for a car pool
carpool_capacity = cars_driven * space_in_a_car

# Compute or calculate the average number of passengers allowed in a car in whole number/integer
average_passengers_per_car = passengers / cars_driven

#  Print statement goes here

print(f"There are {cars} cars available.")
print(f"There are only {drivers} drivers available.")
print(f"There will be {cars_not_driven} empty cars today.")
print(f"We can transport {carpool_capacity} people today.")
print(f"We have {passengers} passengers to carpool today.")
print(f"We need to put about {round(average_passengers_per_car)} passengers in each car.")
