def print_triangle_1(n):  # n = 9
    for i in range(n): # 0, 1, 2, 3, 4, 5 ... 8
        if i == 0:
            print("*")
        elif i == 1:
            print("**")
        elif i == n-1:
            print("*" * (i + 1))
        else:
            print("*" + " " * (i + 1 - 2) + "*")

def print_triangle_2(n):  # n = 9
    for i in range(n): # 0, 1, 2, 3, 4, 5 ... 8
        print("*" * (i + 1))

print_triangle_1(6)
# print("*" + " " * i + "*")
# i 第几行
# 0 1 *
# 1 2 **
# 2 3 * *
# 3 4 *  *
# 4 5 *   *
# 5 6 ******