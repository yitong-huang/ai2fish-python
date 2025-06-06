# 斐波那契数列
# 0 1 1 2 3 5 8 13
# 获取第n个数

# 递归
# f(n) = 0    n = 0
# f(n) = 1    n = 1
# f(n) = f(n-1) + f(n-2)  n>=2
# == 判断是否相等 True / False
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)

print(f(4))

# 阶乘
# f(n) = 1    n = 1
# f(n) = n * f(n-1)  n > 1

# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!
# f(n) = n * f(n-1)
def g(n):
    if n == 1:
        return 1
    else:
        return n * g(n-1)

print(g(5))