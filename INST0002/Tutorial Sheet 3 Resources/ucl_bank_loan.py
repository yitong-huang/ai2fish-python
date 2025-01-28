#!/usr/bin/env python

# Author: Danny Onah
# Date: 20 January 2023
# Time: 03:46AM GMT
"""
UCL Bank loan program...
"""

# print a welcome message


# prompt customer to enter their income per year in pounds
income = float(input("income per year in pounds: "))
# check the condition using the brief in the tutorial sheet
# display the output accordingly
if income >= 100_000:
    print("xxx")
elif income >= 50000:
    print("yyy")
else:
    print("zzz")