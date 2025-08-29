#
# total = 0
# while True:
#     user_input = input('please input a number, or quit to exit: ')
#     if user_input.upper() == 'QUIT':
#         break
#     try:
#         total = total + float(user_input)
#         print(f'current total: {total}')
#     except ValueError:
#         print('input is not a number')

# a = -10
# while a <= 10:
#     b = -120
#     while b <= 120:
#         if a * b == 120:
#             print(f'{a}, {b}')
#             break
#         b += 1
#     a += 1
#
#
# rows = 5
# num = 1
#
# for i in range(rows):
#     for j in range(i + 1):
#         print(f"{num}", end="\t") # 制表符
#         num += 1
#     print()

# mylist = ["abc", "227b", "99e", "def", "888", "ghi", "JK7"]
# filtered_list = []
#
# for s in mylist:
#     anyDigit = False
#     for c in s:
#         if c.isdigit():
#             anyDigit = True
#             break
#     if not anyDigit:
#         filtered_list.append(s)
#
# print(filtered_list)


# 列表推导式
#
# l = [1, 2, 3]
# r = [i for i in l if i % 2 == 0]
# print(r)

# s = "abc8"
# print([c.isdigit() for c in s])

#
# mylist = ["abc", "227b", "99e", "def", "888", "ghi", "JK7"]
# filtered_list = []
# for s in mylist:
#     if not any(c.isdigit() for c in s):
#         filtered_list.append(s)
# print(filtered_list)
#
#
# mylist = ["abc", "227b", "99e", "def", "888", "ghi", "JK7"]
# filtered_list = [s for s in mylist if not any(c.isdigit() for c in s)]
# print(filtered_list)

# 5.c
inches = [10, 20, 30, 40]
meters = []
for inch in inches:
    meters.append(inch * 0.0254)
print(meters)

# 5.d
inches = [10, 20, 30, 40]
meters = [inch * 0.0254 for inch in inches]
print(meters)