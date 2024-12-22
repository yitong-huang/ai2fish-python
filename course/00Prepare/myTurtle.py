import turtle
from turtle import *


def goto(x, y):
    turtle.goto(x, y)
    turtle.write(f"({x},{y})")

def star():
    print("star")
    for i in range(0, 5):
        turtle.forward(100)
        turtle.left(144)

wm = turtle.Screen()
speed(2)
wm.setup(750, 750, 0, 0)
wm.onclick(goto)
onkey(star, "s")
listen()
wm.mainloop()