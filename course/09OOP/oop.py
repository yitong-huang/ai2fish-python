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

print(huang.name)


class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run()

cat = Cat()
cat.run()

