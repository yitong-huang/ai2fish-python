## List

### 定义

列表，可以随时添加和删除其中的元素，用``` [] ```表示

```python
students = ["huang", "li", "wang"]
```

### 长度

len()获取list元素的个数

```python
students = ["huang", "li", "wang"]
len(students)
```

### 获取

用索引来获取list中每一个位置的元素，索引从0开始

```python
students = ["huang", "li", "wang"]
print(students[0])
```

超出范围会报错，最后一个元素的索引是``` len(list) - 1 ```

也可以从后访问数组，最后一个元素是-1，倒数第二个是-2，以此类推，同样的超过界限会报错。

### 插入

插入到列表的最后，可以用``` append ```

```python
students = ["huang", "li", "wang"]
students.append("xxx")
```

插入到指定位置，可以用``` insert ```

```python
students = ["huang", "li", "wang"]
students.insert(1, "yyy")
```

### 删除

删除末尾的元素，用``` pop() ```

```python
students = ["huang", "li", "wang"]
students.pop()
```

删除指定位置元素，用``` pop(i) ```

```python
students = ["huang", "li", "wang"]
students.pop(1)
```

### 修改

直接给对应的索引位置赋值就可以了

```python
students = ["huang", "li", "wang"]
students[1] = "xxx"
```

## Tuple

元组，跟list非常相似，但是一旦初始化就不能修改，用``` () ```表示。

```python
a = (1, 2)
b = ()
c = (3, )
```

没有append，insert，pop这些方法，可以通过索引获取值，但是不能修改。

## 元素

元素可以是任意类型，同一个list或者tuple可以有不同的类型。

```python
l = ["abc", 123, ["yi", "tong"], ("hello", "world")]
t = ("abc", 123, ["yi", "tong"], ("hello", "world"))
```




