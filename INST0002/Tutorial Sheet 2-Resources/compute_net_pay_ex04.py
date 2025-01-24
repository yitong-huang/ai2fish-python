#!/usr/bin/env python
# Author : Danny Onah
# Date : 12 Jan 2024
# Time : 11.31AM GMT

"""
This program should print the computation in dollars $ (US Dollars) according to the brief in the tutorial sheet 2 exercise 4.
"""
"""
Brief: For an employee to earn a monthly pay of $1916.40 before any tax deductions, the employee would need to work for 120 hours in a pay period, 
with an hourly rate of $15.97/hour.
"""


# prompt employee to enter the hours and rate


# compute the gross pay dollars ($)

# compute the monthly salary before tax deductions

# compute the tax on the monthly salary pay in dollars($) 


# compute the net pay in dollars ($)
# Remember the net pay is computed after 20% tax deduction.

MONTHS_IN_YEAR = 12
TAX_RATE = 0.20

hours = float(input("Please enter your hours: "))
rate = float(input("Please enter your rate: "))

monthly_gross = hours * rate
annual_gross = monthly_gross * MONTHS_IN_YEAR
tax_deduction = round(monthly_gross * TAX_RATE, 2)
net_pay = round(monthly_gross - tax_deduction, 2)

print('Your annual gross pay(gross income): ${:g}'.format(annual_gross))
print('Your monthly salary before tax deduction is: ${:g}'.format(monthly_gross))
print('Your 20% tax deduction: ${:g}'.format(tax_deduction))
print('Your take-home (net-pay) after the tax deduction is: ${:g}'.format(net_pay))


