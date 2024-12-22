## Dict

字典。使用键-值（key-value）形式存储，具有极快的查找速度。用``` {} ```表示。

```python
grade = {"huang": 90, "li": 80, "wang": 90}
print(grade["huang"])
```

### 插入

可以通过key插入值

```python
grade = {"huang": 90, "li": 80, "wang": 90}
grade["xxx"] = 100
```

如果key已经存在，则不插入新的值，而是修改原有的

```python
grade = {"huang": 90, "li": 80, "wang": 90}
grade["huang"] = 95
```

### 获取

* 直接用```[key]```

```python
grade = {"huang": 90, "li": 80, "wang": 90}
print(grade["huang"])
```

key不存在时是会报错

```python
grade = {"huang": 90, "li": 80, "wang": 90}
print(grade["yy"])
```

 * 用``` get(key) ```

```python
grade = {"huang": 90, "li": 80, "wang": 90}
print(grade.get("huang"))
print(grade.get("yyy"))
print(grade.get("yyy", 0))
```

### 判断key是否存在

用``` in ```

```python
grade = {"huang": 90, "li": 80, "wang": 90}
print("huang" in grade)
print("yyy" in grade)
```

## Set

set和dict类似，也是一组key的集合，但不存储value。不会有重复的key。两种定义set的方法：

* 用``` {} ```表示。

```python
s = {1, 2, 3}
```

* 用set()，提供一个list

```python
s = set([1, 2, 3])
```

### 插入``` add(key) ```

```python
s = {1, 2, 3}
s.add(10)
s.add(3)
```

### 删除

```python
s = {1, 2, 3}
s.remove(3)
```


