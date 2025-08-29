# def mean(data):
#     if len(data) == 0:
#         return None
#     return sum(data) / len(data)
#
# m = mean([1, 2, 3, 4, 5, 6])
# print(m)
# m = mean([])
# print(m)
#
# def median(data):
#     if len(data) == 0:
#         return None
#     sorted_data = sorted(data)
#     if len(sorted_data) % 2 == 0:
#         return (data[int(len(sorted_data) / 2)] + data[int(len(sorted_data) / 2 - 1)]) / 2
#     else:
#         return data[int((len(sorted_data) - 1) / 2)]
#
#
# m = median([1, 3, 24, 57, 79, 88])
# print(m)
# m = median([])
# print(m)
#
#
# def mode(data):
#     if len(data) == 0:
#         return None
#     number_occurrence = {}
#     for number in data:
#         if number in number_occurrence:
#             number_occurrence[number] += 1
#         else:
#             number_occurrence[number] = 1
#
#     max_occurrence = 0
#     max_occurrence_number = None
#     for number, number_occurrence in number_occurrence.items():
#         if number_occurrence > max_occurrence:
#             max_occurrence = number_occurrence
#             max_occurrence_number = number
#
#     return max_occurrence_number
#
# m = mode([1, 2, 3, 1, 3, 1])
# print(m)
# m = mode([])
# print(m)
#
# def rank(data, number):
#     sorted_data = sorted(data)
#     for i in range(len(sorted_data)):
#         if number == sorted_data[i]:
#             return i
#     return None
#
# m = rank([1, 2, 3, 1, 3, 1], 5)
# print(m)

# l = ["1", "5", "3", "8", "4", "11", "22"]
# sorted_l = sorted(l)
# print(sorted_l)
# max_l = max(l)
# print(max_l)
#
# def numeric_key(value):
#     return float(value)
#
# l = ["1", "5", "3", "8", "4", "11", "22"]
# sorted_l = sorted(l, key=numeric_key)
# print(sorted_l)
# print(l)
# max_l = max(l, key=numeric_key)  # key value
# print(max_l)
# min_l = min(l, key=numeric_key)
# print(min_l)
# l.sort(key=numeric_key)
# print(l)
#
# s = 'hello world'
# arr = s.split()
# print(arr)

# def sort_key(value):
#     return 10 - value
#
# l2 = [1, 3, 5, 2, 4, 6]
# sorted_l = sorted(l2)
# print(sorted_l)

import math

  # global
#
# def f():
#     global x
#     x = 5  # global
#     print(x)
#
# f()
# print(x)

# def area(side, key):
#     return key(side * side)
# #   return print(10 * 10)
# n = area(key=print, side=10)
# print(n)


# def f():
#     return print(100)
#
# n = f()
# print(n)
# arguments

def f(hint, *args):
    for arg in args:
        print(arg, hint)

f("hello", 1,2,3,4,5)