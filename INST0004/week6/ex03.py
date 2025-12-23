#!/usr/bin/env python3
# Author: Danny Onah
# Date: 4 Nov. 23
# Time: 00:33AM GMT

"""
A program for a scrabble game using class and object.
"""

class ScrabbleGame:
    # Global dictionary of letter points
    points = {
        'd': 2, 'g': 2,
        'b': 3, 'c': 3, 'm': 3, 'p': 3,
        'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
        'k': 5,
        'j': 8, 'x': 8,
        'z': 10, 'q': 10,
        'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1,
        'r': 1, 's': 1, 't': 1, 'u': 1
        # letters not listed will default to 0 if needed
    }

    def scrabbleScore(self, word):
        """Recursively compute the Scrabble score of a word."""
        if len(word) == 0:
            return 0
        first_char = word[0].lower()
        score = self.points.get(first_char, 0)
        return score + self.scrabbleScore(word[1:])

    def numberOfVowels(self, word):
        """Recursively count number of vowels in the word."""
        vowels = 'aeiou'
        if len(word) == 0:
            return 0
        first_char = word[0].lower()
        count = 1 if first_char in vowels else 0
        return count + self.numberOfVowels(word[1:])

def main():
    game = ScrabbleGame()
    word = input("Please type a word: ")
    score = game.scrabbleScore(word)
    vowels = game.numberOfVowels(word)
    print(f"The word '{word}' is worth {score} points in Scrabble.")
    print(f"The word '{word}' has {vowels} vowel(s)")

if __name__ == "__main__":
    main()
