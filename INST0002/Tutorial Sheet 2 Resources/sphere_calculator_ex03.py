 #!/usr/bin/env python

 # Author: Daniel Onah
 # Date: 4 January 2023
 # Time: 04:50AM GMT
 
"""
A program to compute the diameter, area and volume of a sphere
"""

# import the math library package

 # print statement to take user input



# perform the arithmetic operation


# print the results

import math

r = int(input("Please input the radius: "))

d = 2 * r
a = 4 * math.pi * r * r
v = 4 / 3 * math.pi * r ** 3

print("The diameter of the sphere is: d = ", d)
print("The surface area of the sphere is: a = ", a)
print("The volume of the sphere is: v = ", v)