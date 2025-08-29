filename = 'gettysburg.txt'
try:
    with open(filename, 'r') as file:
        lines = file.readlines()

        num_lines = len(lines)
        total_words = 0
        total_chars = 0

        for line in lines:
            words = line.replace(',', '').replace('.', '').replace('-', ' ').split()
            total_words += len(words)
            for word in words:
                total_chars += len(word)

        if total_words > 0:
            avg_word_length = total_chars / total_words
        else:
            avg_word_length = 0

        print(f"number of words: {total_words}")
        print(f"Average length of words: {avg_word_length:.2f}")
        print(f"Number of lines: {num_lines}")
except FileNotFoundError:
    print(f"Error: {filename} is not exist.")
except Exception as e:
    print(f"Error: {str(e)}")