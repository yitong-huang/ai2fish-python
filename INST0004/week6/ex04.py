#!/usr/bin/env python3
# Author: Danny Onah
# Date: 3 Sept 2022

# class StringTester:
def d(word):
    """Display first, third, last characters and second half of the word."""
    first_char = word[0]
    third_char = word[2]
    last_char = word[-1]
    second_half = word[len(word) // 2:]

    print(f"The first character of the '{word}' is: {first_char}")
    print(f"The third character of the '{word}' is: {third_char}")
    print(f"The last character of the '{word}' is: {last_char}")
    print(f"The second half of the word '{word}' is: {second_half}")

def main():
    # tester = StringTester()

    while True:
        word = input("Type in a word with at least 6 letters: ")
        if len(word) < 6:
            print("The required length of word is 6 character or above.")
        else:
            d(word)
            break

if __name__ == "__main__":
    main()
