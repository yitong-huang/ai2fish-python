#!/usr/bin/env python

# Author: Danny Onah
# Date: 22 February 2023
# Time: 16:30PM GMT

"""
A program to check list initialisation exception
"""

def listInitialisation(length):
    elements = []
    for i in range(length):
        while True:
            try:
                item = input(f"Enter element in index[{i}]: ")
                elements.append(item)
                break  # Exit loop if input is valid
            except Exception as e:
                print("Invalid entry. Please try again.")
    return elements

def printList(elements):
    print("Displaying elements:")
    for item in elements:
        print(item)

# define the main() function
def main():
    while True:
        try:
            length = input("Enter length of list: ")
            if length == "-1":
                print("Goodbye!")
                break
            length = int(length)
            elements = listInitialisation(length)
            print("List is now full!")
            print("List elements are:", elements)
            printList(elements)
        except ValueError:
            print("Invalid entry! Please enter an integer only.")

main()
    # declare a global variable for the integer number
   
   # use a while loop construct here
  
        # use the try and except construct

            # prompt user for input
          
            # check the condition if the user entered -1
           
                # display a GoodBye message
               
                # terminate the program
               
            # create a variable to store the result from the listInitialisation() function call
            
            # display the result
           
            # call the printList() function

            # display the message to capture a non-integer entry for the length
            
          
# define the listInitialisation() function with one parameter list
# complete the function

    # declare the list as global
  
    # declare the empty list
  
    # use a for-loop and passed the length as part of the argument 
   
        # prompt the user to enter element 
        
        # add the element to the list
        
        # return the empty list
   

# define the printList() with no parameter list
# complete the function
    
       
        # print the elements in the list
      

# call the main() function here to execute the program
