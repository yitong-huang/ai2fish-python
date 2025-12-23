#!/usr/bin/env python3
# Author: Danny Onah
# Date: 3 Sept 2022

class TriangularNumber:
    def triangularGenerator(self, number):
        """Recursively compute the nth triangular number."""
        if number <= 1:  # Base case: T(1) = 1, T(0) = 0
            return number
        else:
            return number + self.triangularGenerator(number - 1)

def main():
    try:
        num = int(input("Type in an integer: "))
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            generator = TriangularNumber()
            result = generator.triangularGenerator(num)
            print(f"The triangular number of '{num}' is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
