try:
    with open("gettysburg.txt") as f:
        total_words = 0
        total_chars = 0
        total_lines = 0

        for l in f:
            words = l.replace(",", " ").replace(".", " ").replace("-", " ").split()
            total_words += len(words)
            for word in words:
                total_chars += len(word)
            total_lines += 1

        if total_words == 0:
            avg_word_length = 0
        else:
            avg_word_length = total_chars / total_words

        print(f"The number of words: {total_words}")
        print(f"Average length of words: {avg_word_length}")
        print(f"Number of lines: {total_lines}")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission error")
except Exception as e:
    print("Something went wrong", e)

print("=====")

try:
    with open("words.txt", "r") as f, open("five_letter_words.txt", "w") as g:
        origin_file_name = 0
        new_file_line = 0
        for line in f:
            origin_file_name += 1
            line = line.strip()
            if len(line) == 5:
                g.write(line + "\n")
                new_file_line += 1
        print(f"number of words in the original file: {origin_file_name}")
        print(f"number of words in the new file: {new_file_line}")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission error")
except Exception as e:
    print("Something went wrong", e)

