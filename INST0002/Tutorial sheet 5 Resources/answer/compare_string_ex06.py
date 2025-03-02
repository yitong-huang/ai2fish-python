#/usr/bin/env python

# Author: Danny Onah
# Date: 4 Feb2023
# Time: 04:43AM GMT

"""
A program to compare two or more strings
"""
string1 = "119"
string2 = "19"

# use the description in the tutorial sheet 5 brief to work on this task.

# Compare string1 and string2
if string1 == string2:
    comparison = "is the same as"
else:
    comparison = "is not the same as"

# Print the comparison result for string1 and string2
print(f"The strings '{string1}' {comparison} the string '{string2}'.")

# Create string3 by concatenating string2 with "1"
string3 = "1" + string2

# Check if string1 is not equal to string3
if string1 != string3:
    comparison_message = "not"
else:
    comparison_message = ""

# Print the result of the comparison between string1 and string3
print(f"The strings '{string1}' and '{string3}' are identical." if comparison_message == "" else f"The strings '{string1}' is {comparison_message} the string '{string3}'.")