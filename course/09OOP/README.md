## Object Oriented Programming 面向对象编程

把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数

面向过程的程序设计是一系列命令的集合，即一组函数的顺序执行。  
为了简化程序设计，我们会把过程切成成子函数。

面向对象的程序设计是一组对象的结合，每个对象都可以接收其他对象发过来的消息，并处理这些消息。  
计算机程序的执行就是一系列消息在对象之间传递。

### 例子：

处理学生成绩时，如果是面向过程，我们可以用一个dict表示

```python
std1 = { 'name': 'huang', 'score': 98 }
std2 = { 'name': 'li', 'score': 81 }
```

如果要打印学生成绩，可以定义函数：

```python
def print_score(std):
    print(std['name'], std['score'])
```

如果是面向对象，我们会先定义一个学生Student的类，它有name和score两个属性。  
如果要打印一个学生的成绩，首先要创建这个学生对应的对象，然后给它发一个print_score的消息，对象自己把数据打印出来：

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(self.name, self.score)

# 创建对象及调用对象的函数
huang = Student('huang', 59)
li = Student('li', 87)
huang.print_score()
li.print_score()
```

### 类

定义类的关键字是```class```。

构造方法```__init__```

普通方法

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(self.name, self.score)
```

### 对象

```python
huang = Student('huang', 80)
```

### 访问限制

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线```__```

这时候，我们通常会给类增加set和get方法

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def print_score(self):
        print(self.name, self.__score)

    def set_score(self, score):
        self.__score = score
```

为什么要限制访问呢？

### 继承和多态

当我们定义一个class的时候，可以指定继承自某个现有的class。  
新的class成为子类，被继承的成为父类（或者基类）

```python
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass
```

当子类和父类都存在相同的```run()```方法时，我们说，子类的```run()```覆盖了父类的```run()```。

在代码运行的时候，总是会调用子类的run()，称为多态。

这样有什么好处？

### 获取对象信息

#### 使用```type()```

#### 使用```isinstance()```

### 实例属性和类属性

```python
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name

```

实例属性属于各个实例所有，互不干扰；

类属性属于类所有，所有实例共享一个属性；

不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。