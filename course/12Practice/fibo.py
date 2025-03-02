# # # fibonacci 斐波那契数列
# # # 1 1 2 3 5 8 13
# # # list []
# #
# def fibonacci(n):
#     result = []
#     for i in range(n):
#         if i == 0:
#             result.append(1)  # result = [1]
#         # 如果i是0，那么result增加一项1
#         elif i == 1:
#             result.append(1)
#         # 如果i是1，那么result增加一项1
#         else:
#             result.append(result[-1] + result[-2])
#     return result
#
# l = fibonacci(6)
# print(l)



# l1 = [1,  2,  3]
# l2 = [-1, -2, -2, 4, 5]

# l =  [0,  0,  1,  4, 5]

def add_list(l1, l2):
    l = []
    # 两个数组相加
    l = l1 + l2
    return l

l1 = [1,  2,  3,  4,  5]
l2 = [-1, -2, -2]
l = add_list(l1, l2)
print(l)

