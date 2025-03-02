#!/usr/bin/env python
# Author: Danny Onah
# Date: 22 February 2023
# Time: 02:54AM GMT

"""
A program to check whether a list item is a clean source of energy
"""


def find():
    clean_energy = ["Solar", "Wind", "Hydrogen", "Tidal"]

    while True:
        energy = input("Enter energy source: ")

        if energy.lower() == "done":
            print("Goodbye!")
            break

        energy = energy.title()  # Convert input to title case

        if energy in clean_energy:
            print(f"Yes, {energy} is a clean source of energy")
        else:
            print(f"No, {energy} is NOT a clean source of energy")

find()
        # list is case sensitive, ensure you convert to title case before searching
        
        # prompt user for input .. energy name
       
        # check if the user entered the word done
        # display Goodbye and end the program
       
        # convert the input into title case if upper or lower case entered
        
        # check whether the energy entered by the user is a clean energy source
       
            # display the message if true here
          
            # otherwise display a message if not true
