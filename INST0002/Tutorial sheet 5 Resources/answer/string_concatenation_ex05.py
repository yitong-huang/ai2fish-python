# Author: Danny Onah
# Date: 4 Feb.2023
# Time: 04:10AM GMT

# declare two strings
string1 = "super"
string2 = "person"
# concatenate the two strings with space

# print the characters of the string2 from index 0 to index 3 (4 character position)

# use the substitution function to substitute the character Z with the first character in index 0 (position 1)


# Concatenate string1 and string2 with a space in between
concatenated_string = string1 + " " + string2
print(f"Concatenation: {concatenated_string}")

# Extract the 0th to 3rd characters (inclusive) of string2
substring = string2[:4]
print(f"0th to 3rd letters (inclusive): {substring}")

# Create a new string which is the same as string1 except the 0th character is "Z"
replaced_string = "Z" + string1[1:]
print(f"Replaced first character of string1: {replaced_string}")