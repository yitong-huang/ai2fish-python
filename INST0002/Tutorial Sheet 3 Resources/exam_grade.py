 #!/usr/bin/env python
"""
Grading System program use the if, elif, else statement to compute the final average grade
"""
# Author: Daniel Onah 
# Date: 30 Dec. 2022
# Time: 02.37AM GMT



average = 0
grade = 0
graded_mark = 0

# Prompt the student for input
modules = int(input("How many modules do you have: "))

# initialise the for-loop iteration (i) by 1
total = 0
try:
    for i in range(modules):
        grade = int(input("Please enter the grade for module number {}: ".format(i + 1)))
        if grade < 0:
            print("You have entered a negative number", grade)
            print("Please enter only positive integer grades. Thank you!")
            print("Your average grade is: 0")
            print("Fail")
        total = total + grade
    average = total / modules
    print("Your cumulative GPA is:", average)
except ValueError:
    print("Please enter only positive integer grades. Thank you!")
    print("Your average grade is: 0")
    print("Fail")


# define your for-loop construct here

# use a try and except block for this process to check for any mismatch entry (use the knowledge from the Lecture)
#        try:
# compute the sum total of all grades entered


# compute the average of the grades

# All these computation should be inside the try and except block

        # except ValueError:
               # display the  message to be captured here


# Display the result of the GPA calculated         
 # round the grade to 2 decimal places

 # check this average grade with condition for each classification

 # print the classification and the GPA at the end.

 # if no grades were entered , output the appropriate message
                      
       
    
    

