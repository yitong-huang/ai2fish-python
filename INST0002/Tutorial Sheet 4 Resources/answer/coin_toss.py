#!/usr/bin/env python

# Author: Danny Onah
# Date: 27 Jan.23
# Time: 18:39PM GMT

"""
A program to perform the operation of virtual coin toss
"""
# import the random module
import random

# define the main function
def coin_tosses(num_tosses):
    heads = 0  # 计数
    tails = 0
# define a flipCoin() function
    for _ in range(num_tosses):
        flip = random.randint(0, 1)  # 0 is heads, 1 is tails
        if flip == 0: #
            # heads1 = heads + 1
            heads = heads + 1
        else:
            tails += 1

    return heads, tails

# declare a random number
# this should produce random numbers from 0 - 1 limit
def main():
    num_tosses = int(input("How many coin flips? : "))
    heads, tails = coin_tosses(num_tosses)

# use a for-loop for the task here
    print(f"Number of Heads is: {heads}")
    print(f"Number of Tails is: {tails}")

# start the program here
main()
