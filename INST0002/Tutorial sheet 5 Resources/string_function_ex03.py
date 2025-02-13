"""
A program to use function to compute a string sentence
"""

# Author: Danny Onah
# Date: 3 Feb 2023
# Time: 00:42PM


# define your main function here. Do ensure you understand the task requirements  as presented in the TS5 brief.

    

# Functions to support the operation and change the behaviour of the program
def break_words(sent):
    """ This function will break up the words in the sentence """
    words = sent.split(' ')
    return words

def sort_words(words):
    """ This function will sort the words in the string sentence. """
    return sorted(words)

def print_first_word(words):
    """ This function will print out the first word after popping it off. """
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """ This function print the last word after popping it off. """
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """ This function should take in the full sentence and return the sorted words. """
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """ This function should print the first and last words of the sentence. """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """ This function should sort the words prints the first and last words in the sentence. """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words) 

