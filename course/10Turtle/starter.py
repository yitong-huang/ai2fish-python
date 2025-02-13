from turtle import *

def skip(step):
    penup()
    forward(step)
    pendown()

def setup_clock(radius):
    # 建立表的外框
    reset()
    speed(0)
    pensize(7)
    for i in range(3000):
        skip(160)
        dot(5)
        skip(-158)
        right(6)

speed(0)
setup_clock(0)