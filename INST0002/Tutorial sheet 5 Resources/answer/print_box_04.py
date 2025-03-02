# Author: Danny Onah
# Date: 4 Feb.2023
# Time: 03:39AM GMT


# define a function called box_print(), this function should take three input parameters.
    # check the condtion for the symbol here (ensure the length is not equal to 1)
    
        # raise the exception message here
    # define the if condtion for width
        # raise the exception message here
   # define the if condition for height
        # raise the exception message here
# create a for-loop for the first iteration
def print_box(symbol, width, height):
    # Check if symbol is a single character string.
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string")

    # Check if the width is greater than 2.
    if width <= 2:
        raise Exception("Width must be greater than 2")

    # Check if the height is greater than 2.
    if height <= 2:
        raise Exception("Height must be greater than 2")

    # Loop to print the box with given width and height.
    # First and last lines
    print(symbol * width)

    # Middle lines (height-2 lines)
    for _ in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)

    # Last line (same as first line)
    print(symbol * width)

# tuple
# Main program that tests the function with multiple boxes and exception handling
def main():
    boxes = [
        ('*', 4, 4),
        ('O', 20, 5),
        ('x', 3, 2),
        ('Z', 3, 3)
    ]

    for symbol, width, height in boxes:
        try:
            print_box(symbol, width, height)
            print()  # Blank line after each box
        # call the function and pass in the arguments (i.e. symbol, width and height)

        except Exception as err:
           print('An exception happened: ' + str(err))

main()

# create the for loop containing the symbols, width and height of the box as input arguments

    # use a try and except of exception to handle the error message
