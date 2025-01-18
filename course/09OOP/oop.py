std1 = { 'name': 'huang', 'score': 98 }
std2 = { 'name': 'li', 'score': 81 }

def print_score(std):
    print(std['name'], std['score'])

print_score(std1)
print_score(std2)
# 0 - 100
# 父类
class Student(object):
    def __init__(self, name, score):
        self.name = name
        if score < 0 or score > 100:
            print("warning")
            self.__score = -1
        else:
            self.__score = score

    def print_score(self):
        print(self.name, self.__score)

    def set_score(self, score):
        if score < 0 or score > 100:
            print("warning")
            self.__score = -1
        else:
            self.__score = score


li = Student('li lili', 87)

li.set_score(1000)
li.print_score()
li.name = "####"
li.print_score()

# 定义一个类，类名是Animal，
# 两个属性名字，速度
# 有一个方法，run，打印 名字 run at speed 速度
class Animal(object):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def running(self):
        print(self.name, "run at speed", self.speed)

dog = Animal("kiki", 10)
dog.running()


class Animal(object):
    def eat(self):
        print('Animal is eating')

class Runnable(object):
    def run(self):
        print('running')

class Dog(Animal, Runnable):
    def wangwang(self):
        print("Dog is wangwang")
    def run(self):
        print("Dog is running")

class Elephant(Animal):
    pass

# 多重继承

kiki = Dog()
kiki.run()
kiki.eat()
# e.run()
