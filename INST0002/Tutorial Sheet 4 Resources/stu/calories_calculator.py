#!/usr/bin/env python

# Author: Danny Onah
# Date: 27 Jan.23
# Time: 17:46PM GMT
"""
A program to calculate the calories burnt walking and climbing
"""

# define the function calculateCaloriesWalking()
def calculate_walking_calories(bw, s, t, h):
    walking_calories = t * ((0.035 * bw) + ((s ** 2) / h * 0.029 * bw))
    return walking_calories

# define the function calculateCaloriesClimbing()
def calculate_stair_climbing_calories(bw, t):
    t_in_hours = t / 60
    stair_climbing_calories = 6.2 * bw * t_in_hours
    return stair_climbing_calories

# define the main() function
def main():
    bw = float(input('Enter bodyweight (kg): '))
    h = float(input('Enter height (m): '))
    s = float(input('Enter average walking speed (m/s): '))
    t_walk = float(input('Enter time walked (min): '))
    t_climb = float(input('Enter time climbing stairs (min): '))

    walking_calories = calculate_walking_calories(bw, s, t_walk, h)
    stair_climbing_calories = calculate_stair_climbing_calories(bw, t_climb)

    print(f"The number of calories burnt walking is: {walking_calories:.2f}")
    print(f"The number of calories burnt climbing is: {stair_climbing_calories:.2f}")


# start the program with a main()
main()