from turtle import *
from datetime import *

def skip(length):
    penup()
    forward(length)
    pendown()

def register_hand(name, length):
    reset()
    begin_poly()
    forward(length)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)

def init():
    global sec_hand, min_hand, hour_hand
    mode("logo")
    register_hand("sec_hand", 150)
    register_hand("min_hand", 125)
    register_hand("hour_hand", 90)
    sec_hand = Turtle()
    sec_hand.shape("sec_hand")
    sec_hand.pencolor("red")
    min_hand = Turtle()
    min_hand.shape("min_hand")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    for hand in sec_hand, min_hand, hour_hand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)

def setup_clock(radius):
    reset()
    pensize(7)
    for i in range(60):
        skip(radius)
        if i % 5 == 0:
            forward(20)
            skip(-radius - 20)
        else:
            dot(5)
            skip(-radius)
        right(6)

def tick():
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    sec_hand.setheading(6 * second)
    min_hand.setheading(6 * minute)
    hour_hand.setheading(30 * hour)
    ontimer(tick, 1)

def main():
    tracer(False)
    init()
    setup_clock(160)
    tracer(True)
    tick()
    done()

main()