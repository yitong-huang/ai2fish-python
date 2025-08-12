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
rows = 5
num = 1

for i in range(rows):
    for j in range(i + 1):
        print(f"{num}", end="\t") # 制表符
        num += 1
    print()