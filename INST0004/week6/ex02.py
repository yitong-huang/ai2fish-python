def fact(numb):
    """Recursive function to compute factorial of a number."""
    if numb == 1 or numb == 0:  # Base case: 0! and 1! are both 1
        return 1
    else:
        return numb * fact(numb - 1)  # Recursive case

try:
    index = int(input("Enter number: "))
    if index < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = fact(index)
        print(f"The factorial of {index}! is: {result}")
except ValueError:
    print("Please enter a valid integer.")


