#!/usr/bin/env python

# Author: Danny Onah
# Date: 17 Feb.23
# Time: 11:34AM GMT

"""
A program to use sequential or linear search approach
"""

def main():
    user_input = input("Please enter your statement: ")

    sentence = user_input.split()

    for word in sentence:
        print(word)

    if "list" in sentence or "lists" in sentence:
        print("You have learnt something about lists. Well done!")
    else:
        print("Practice and study more about using lists in Python!")

main()

# define the function here


 # use the 'in' keyword to check if word is in the strings
			

# create empty list to store the sentence

# prompt user for the sentence

# add the sentence to the list

# use the split function to split the sentence before search 

# use a for loop

	# split the sentence 
	
	# print the elements in the list

# declare the word or words and initialise this by 'list' or 'lists'

# check the condition and display the outcome 
	