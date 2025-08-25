 #!/usr/bin/env python

 # Author: Daniel Onah
 # Date: 4 January 2023
 # Time: 04:12AM GMT

"""
A program to compute the number of calories burnt
"""
# take the input from the user
# considering the various data.txt types as required in the tutorial sheet brief

bw = float(input("Please enter bodyweight (kg): "))
h = float(input("Please enter height (m): "))
s = float(input("Please enter average speed (m/s): "))
t = float(input("Please enter time walked (min): "))

tcb = t * ((0.035 * bw) + (s ** 2 / h * 0.029 * bw))

print("The number of calories burnt is: %.1f"%tcb)

# perform the operation using the formula to calculate the calories burnt
