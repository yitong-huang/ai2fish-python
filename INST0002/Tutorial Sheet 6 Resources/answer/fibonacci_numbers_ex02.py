#!/usr/bin/env python

# Author: Danny Onah
# Date: 17 Feb.23
# Time: 13:00PM GMT

"""
A program to compute the Fibonacci number series
"""
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(3, n+1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    n = int(input("How long the Fibonacci sequence should be? : "))
    fib_list = fibonacci(n)
    print(" ".join(map(str, fib_list)))

main()



	# create a global variables that could be used easily by
	# both main and fibonacci functions
	
	# call the fibonacci function passing the list as argument
	

	# use a for-loop to iterate over the number stored in the empty list
	# and display the fibonacci number sequence in the body of the loop
	
	# disply the numbers vertically
		#print(i) # displays the number horizontally

#define the fibonacciNumbers() function	


	# initialise the previous number and current number with 0 & 1 accordingly
	
	# add the previous and current number to the empty list
	# this should be part of the fibonacci series
	

	
		# sum the previous number and the current number
		
		# using the append function to add the sum to the empty list
		
		# assign the current number to the previous number
		
		# assign the sum of both numbers to the current number
		
