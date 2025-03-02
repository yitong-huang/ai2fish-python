#!/usr/bin/env python

# Author: Danny Onah
# Date: 17 Feb.23
# Time: 15:13PM GMT

"""
A program to compare lists
"""


def compare(list1, list2):
    list1.sort()
    list2.sort()

    if list1 == list2:
        print("You have friends in common!")
    else:
        print("Your friends are different!")

def main():
    user1_friends = ["Danny", "Elaine", "Jane"]
    user2_friends = ["Jane", "Elaine", "Danny"]

    print("Friends of user1 are:")
    for friend in user1_friends:
        print(friend)

    print("Friends of user2 are:")
    for friend in user2_friends:
        print(friend)

    compare(user1_friends, user2_friends)

main()

# define the function

	# display the message for user 1 friends
	
	# use for-loop to check whether friend exists
	
		# print sorted friends
		
	# display the message for user 2 friends
	

	# use for-loop to check whether friend exists
	
		# display the message for user 2 friends
		
# check whether the friends in user 1 is same as user 2
	
# declare and initialise the list of friends


# sort the friends

# compare the friends


