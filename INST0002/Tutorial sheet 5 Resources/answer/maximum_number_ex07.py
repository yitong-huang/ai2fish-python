 #!/usr/bin/env python

 # Author: Daniel Onah
 # Date: 03 Dec.2023
 # Time: 02:23AM GMT

 # A program to find the maximum number of three input numbers
 # The program should be able to return the maximum number of the three input numbers
 # ... Without using the Python built-in  max() function


# The print statement allows you to print the max number
# Ensure you define the function first before calling it in your program


 # Define the user-defined function to find the maximum number
 # 驼峰 风格
def findMaximumNumber(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


 # Main program to input three integers from the user
def main():
     # Prompt the user for input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

     # First, find the maximum between num1 and num2
    max_of_two = findMaximumNumber(num1, num2)

     # Now, find the maximum between the result and num3
    maximum_number = findMaximumNumber(max_of_two, num3)

     # Display the maximum number
    print(f"The maximum number is: {maximum_number}")

main()