import string

def remove_punctuation(text):
    """Removes punctuation from the input text."""
    return text.translate(str.maketrans('', '', string.punctuation))

def recursiveWordCount(words, target):
    """Recursively counts occurrences of target in the words list."""
    if not words:  # base case: no words left
        return 0
    elif words[0] == target:  # first word matches target
        return 1 + recursiveWordCount(words[1:], target)
    else:  # first word doesn't match
        return recursiveWordCount(words[1:], target)

def main():
    # Input from user
    target = input("Enter the word to count: ")
    sentence = input("Enter a sentence: ")

    # Normalize input: remove punctuation and convert to lowercase
    target = remove_punctuation(target).lower()
    sentence = remove_punctuation(sentence).lower()

    # Split sentence into words
    word_list = sentence.split()

    # Count using recursion
    count = recursiveWordCount(word_list, target)

    # Handle plural/singular properly in output
    instance_word = "instance" if count == 1 else "instances"
    print(f"The sentence contains {count} {instance_word} of the word '{target}'.")

if __name__ == "__main__":
    main()

