# std1 = { 'name': 'huang', 'score': 98 }
# std2 = { 'name': 'li', 'score': 81 }
#
# def print_score(std):
#     print(std['name'], std['score'])
#
# # 面向过程编程
# # 面向对象编程
#
# print_score(std1)
# print_score(std2)
#
# def func1():
#     print("hello world")

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def info(self):
        print(self.name, self.score)

    def x(self, number):
        print("x", number)


stu1 = Student('huang', 98)
stu2 = Student('li', 81)
stu3 = Student('Wang', 85)

stu1.info()
stu2.info()
stu3.info()

stu1.x(100)
stu2.x(200)

# 0 - 100
# 父类
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         if score < 0 or score > 100:
#             print("warning")
#             self.__score = -1
#         else:
#             self.__score = score
#
#     def print_score(self):
#         print(self.name, self.__score)
#
#     def set_score(self, score):
#         if score < 0 or score > 100:
#             print("warning")
#             self.__score = -1
#         else:
#             self.__score = score
#
#
# li = Student('li lili', 87)
#
# li.set_score(1000)
# li.print_score()
# li.name = "####"
# li.print_score()
#
# # 定义一个类，类名是Animal，
# # 两个属性名字，速度
# # 有一个方法，run，打印 名字 run at speed 速度
# class Animal(object):
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#
#     def running(self):
#         print(self.name, "run at speed", self.speed)
#
# dog = Animal("kiki", 10)
# dog.running()
#
#
# class Animal(object):
#     def eat(self):
#         print('Animal is eating')
#
# class Runnable(object):
#     def run(self):
#         print('running')
#
# class Dog(Animal, Runnable):
#     def wangwang(self):
#         print("Dog is wangwang")
#         print("xxxx")
#     def run(self):
#         print("Dog is running")
#
# class Elephant(Animal):
#     pass
#
# # 多重继承
#
# kiki = Dog()
# kiki.run()
# kiki.eat()
#
#
# class Animal(object):
#     def jiao(self):
#         print("jiao")
#
# class Dog(Animal):
#     def __init__(self, n):
#         self.name = n
#     def jiao(self): # 重写 覆盖 override
#         print("wang")
#
# class Cat(Animal):
#     def __init__(self, n):
#         self.name = n
#     def jiao(self):
#         print("miao")
#
# class Elephant(Animal):
#     def __init__(self, n):
#         self.name = n
#
# a = Dog("gou")
# b = Cat("mm")
# c = Animal()
# d = Elephant("ee")
#
# def jiao_twice(l):  # 变量
#     for item in l:
#         item.jiao()
#         item.jiao()
#
# jiao_twice([a, b, c, d])