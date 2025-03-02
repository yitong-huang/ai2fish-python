#!/usr/bin/env python
# Author: Danny Onah
# Date: 22 February 2023
# Time: 01:46AM GMT
"""
A program to compute an arbitrary list of months. 
"""
def main():
    month01 = "January"
    month02 = "February"
    month05 = "May"
    month07 = "July"
    month12 = "December"
    year1 = 2020
    year2 = 2021
    year3 = 2022
    year4 = 2023
    monthsOnLeave(year1, month01, month02, month12)
    monthsOnLeave(year2, month01, month07)
    monthsOnLeave(year3, month01, month05, month07, month12)
    monthsOnLeave(year4, month01, month02, month07, month12)

def monthsOnLeave(year, *months):
    print(f"\nIn {year}, I am on leave in:")
    for i, month in enumerate(months):
        if i == len(months) - 1 and len(months) > 1:
            print(f"and {month}.")
        else:
            print(f"{month},")

main()

# *** add the monthsOnLeave() function here ***

# check lecture 4 function to help you understand how you could take several number of 
# parameters in your function

    # declare and initialise your iteration by zero '0'
    
    # display the print message ' In 2021, I am on leave in: ...'

    # use a for-loop to iterate over the arbitrary months
   
        # increment the iteration
       
        # check the condition that the iteration is not more than the number of months
       
            # print the months on leave for each year
            
     