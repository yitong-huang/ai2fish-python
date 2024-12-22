## 遍历

在python中，通常用``` for ... in ```来遍历

### List和Tuple

```python
students = ["huang", "li", "wang"]
for student in students:
    print(students)
```

```python
levels = ("a", "b", "c", "d")
for level in levels:
    print(level)
```

还可以结合``` enumerate ```同时迭代索引和元素本身

```python
students = ["huang", "li", "wang"]
for i, student in enumerate(students):
    print(i, students)
```

### Dict

可以通过key来遍历字典

```python
grades = {"huang": 80, "li": 70, "wang": 90}
for name in grades:
    print(name, grades[name])
```

也可以同时迭代key和value来遍历字典，用``` for key, value in d.items() ```

```python
grades = {"huang": 80, "li": 70, "wang": 90}
for name, grade in grades.items():
    print(name, grade)
```

### 字符串

字符串也是可迭代的

```python
for c in "hello world":
    print(c)
```
