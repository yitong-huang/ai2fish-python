filename = 'words.txt'
original_count = 0
five_letter_count = 0

try:
    with open(filename, 'r') as file:
        words = file.readlines()
        original_count = len(words)

        five_letter_words = []
        for word in words:
            cleaned_word = word.strip()  # Remove newline characters
            if len(cleaned_word) == 5:
                five_letter_words.append(cleaned_word)
                five_letter_count += 1

        with open('five_letter_words.txt', 'w') as output_file:
            for word in five_letter_words:
                output_file.write(word + '\n')

    # Print results
    print(f"Number of words in original file: {original_count}")
    print(f"Number of 5-letter words: {five_letter_count}")
    print("Five-letter words have been saved to 'five_letter_words.txt'")
except FileNotFoundError:
    print(f"Error: {filename} is not exist.")
except Exception as e:
    print(f"Error: {str(e)}")