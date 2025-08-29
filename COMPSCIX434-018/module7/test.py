# 1
class Rectangle:

    def __init__(self, width, height, name='unnamed', x=0, y=0):
        self.width = width
        self.height = height
        self.name = name
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    def info(self):
        return f"name: {self.name}, x: {self.x}, y:{self.y}, width: {self.width}, height: {self.height}, area: {self.area()}"

    def move(self, x, y):
        self.x = x
        self.y = y



r1 = Rectangle(100, 200)
r2 = Rectangle(200, 400, "r2", 10)
print(r1.info())
print(r2.info())

r1.move(1000, 2000)
print(r1.info())

r2.move(300, 600)
print(r2.info())


## 2
class Vehicle:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.odometer = 0

    def drive(self, minutes):
        distance = self.speed * minutes / 60
        self.odometer += distance
        return distance

v1 = Vehicle("v1", 60)
print(v1.drive(10))
print(v1.odometer)
print(v1.drive(20))
print(v1.odometer)

v2 = Vehicle("v2", 120)
print(v2.drive(10))
print(v2.odometer)
print(v2.drive(20))
print(v2.odometer)


## 3
class Rectangle:

    def __init__(self, width, height, name='unnamed', x=0, y=0):
        self.width = width
        self.height = height
        self.name = name
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    def info(self):
        return f"name: {self.name}, x: {self.x}, y:{self.y}, width: {self.width}, height: {self.height}, area: {self.area()}"

    def move(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        width = self.width + other.width
        height = self.height + other.height
        return Rectangle(width, height)

    def __eq__(self, other):  # == equal
        return self.area() == other.area()

    def __ne__(self, other):  # != not equal
        return self.area() != other.area()

    def __lt__(self, other):  # <  less than
        return self.area() < other.area()

    def __gt__(self, other):  # >  greater than
        return self.area() > other.area()

    def __le__(self, other):  # <=  less equal
        return self.area() <= other.area()

    def __ge__(self, other):  # >= greater equal
        return self.area() >= other.area()

    def __str__(self):
        return self.info()

r1 = Rectangle(300, 400)
r2 = Rectangle(200, 600)
r3 = r1 + r2
print(r1.info())
print(r2.info())
print(r3.info())

print(r1 > r2)
print(r1 < r2)
print(r1 == r2)
print(r1 != r2)
print(r1 >= r2)
print(r1 <= r2)

print(r1)
print(r2)

## 4
class Vehicle:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def drive(self, minutes):
        distance = self.speed * minutes / 60
        return distance

class Bicycle(Vehicle):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.basket = True

class Motorcycle(Vehicle):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.engine = 4

class Truck(Vehicle):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.cargo = 10

    def load(self):
        pass

class HybridCar(Vehicle):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.battery = 100

    def charge(self):
        pass