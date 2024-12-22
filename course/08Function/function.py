print("xxx", 123)
print("abs(-100): ", abs(-100))


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print("my_abs(-100): ", my_abs(-100))

def my_max(a, b):
    if a > b:
        return a
    else:
        return b

print("my_abs(1, 100): ", my_max(1, 100))

def say_hello():
    print("hello world")

say_hello()

def add_all(a, b, c, x):
    return a + x, b + x, c + x

print(add_all(1, 2, 3, 100))