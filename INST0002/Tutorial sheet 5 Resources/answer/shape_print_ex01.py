#!/usr/bin/env python

# Author: Danny Onah
# Date: 27 Jan.23
# Time: 17:46PM GMT
"""
A program to print the shape of an object
"""

# Ensure you use the requiements of the tutorial sheet 5 task brief to complete the task.
c = input('Enter character : ')
size = int(input('Enter size : '))

print()
for i in range(size):
    print(c, end='')

print()
print('Number of chars used: {}'. format(size))
print()

for i in range(size):
    for j in range(size):
        print(c, end='')
    print()

print('Number of chars used: {}'. format(size * size))
print()

for i in range(size):
    for j in range(i+1):
        print(c, end='')
    print()

print()
print('Number of chars used: {}'. format((1 + size) * size / 2))

