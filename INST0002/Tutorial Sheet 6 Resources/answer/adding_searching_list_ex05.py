#!/usr/bin/env python
# Author: Danny Onah
# Date: 21 February 2023
# Time: 23:01PM GMT
"""
A program to search for names in a list and add a name if not found using two functions
"""
#  program with two functions

def search(names):
    while True:
        name = input("Enter name to search for: ")
        if name.lower() in ["done", "finish"]:
            break

        if name in names:
            print(f"The name: {name} is in: index[{names.index(name)}]")
        else:
            print("The name does not exist!")
            add_name = input("Do you want to add this name (yes or no): ").strip().lower()
            if add_name == "yes" or add_name == "y":
                names.append(name)
                print(f"Adding name {name} to position: {len(names) - 1}")
            else:
                print(f"Name {name} NOT added to the list ...")


def main():
    names = ["Danny", "Elaine", "Jane"]
    search(names)
    print("\nThe names are:")
    for index, name in enumerate(names):
        print(f"  The name {name} is in index: {index}")

main()

# define the main function here

    # take the name input
   
    # call the search() function


# define the search() function here

    # initialise a list of names - "Danny" - "Elaine" - "Jane"
   
    # use a loop construct to continously prompt user to enter name
    
        # if the word 'finish' or 'done' is entered as input, 
        # the program should stop requesting for user input and display the result
       
            
        # check whether the name is in the list
       
            # if name not found, print a message asking the user if the want to add the name to the list
            
            # if answer is yes or y
           
                # add the name to the list
                 # list concatenation
                # print a message with the name and the position they are added to.
                
              
                # otherwise display a message that the name is not added
           
           
        # search for a name in the list, if name is found 
        # display the name and the index location number
        
         
    # display all names in the list after the word 'finish' or 'done' is entered
  
  