 #!/usr/bin/env python

# Author: Danny Onah
# Date: 20 January 2023
# Time: 03:30AM GMT
"""
A program to calculate the number of boxes to store apples.
"""


# define a floating-point variable to prompt user for the maximum weight of the box
box_weight = float(input("Enter the maximum weight the box could take: "))

# define a floating-point variable to prompt user for the weight of the apples
apple_weight = float(input("Enter the weight of apples to be boxed: "))

# Divide and take the value in whole number by typecasting the float value to integer
box = int(apple_weight / box_weight)
# box = apple_weight // box_weight

# use a condition to check whether the number of boxes is less than the weight of the apples then
# divide this by the max  weight of the box.
if box_weight * box >= apple_weight:
    print("The number of boxes you need is:", int(box))
else:
    print("The number of boxes you need is:", int(box + 1))

# display the result 
