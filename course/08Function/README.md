## 调用函数

```python
print("xxx", 123)
abs(-100)
```

## 定义函数

定义一个函数要使用def语句，跟着函数名、括号、括号中是参数（非必要，可以有多个）和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回（非必要）。

```python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-100))
```

## 参数

参数可以是零个或多个，多个参数之间用``` , ```隔开，零个参数括号还是要保留。

```python
def my_max(a, b):
    if a > b:
        return a
    else:
        return b

def say_hello():
    print("hello world")
```

## 返回值

可以没有返回，也可以有多个返回值

```python
def say_hello():
    print("hello world")


```
