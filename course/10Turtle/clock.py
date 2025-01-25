from turtle import *
from datetime import *


def skip(step):
    penup()
    forward(step)
    pendown()


def mk_hand(name, length):
    # 注册turtle形状，建立表针turtle
    reset()
    # skip(-length * 0.1)
    begin_poly()
    forward(length)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)


def init():
    global sec_hand, min_hand, hour_hand, printer
    mode("logo")
    # 重置turtle指向北
    # 建立三个表针turtle并初始化
    mk_hand("sec_hand", 150)
    mk_hand("min_hand", 125)
    mk_hand("hour_hand", 90)
    sec_hand = Turtle()
    sec_hand.shape("sec_hand")
    min_hand = Turtle()
    min_hand.shape("min_hand")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    for hand in sec_hand, min_hand, hour_hand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    # 建立输出文字turtle
    printer = Turtle()
    printer.hideturtle()
    printer.penup()


def setup_clock(radius):
    # 建立表的外框
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


def week(t):
    week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]


def date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)


def tick():
    # 绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + second / 60.0
    sec_hand.setheading(6 * second)
    min_hand.setheading(6 * minute)
    hour_hand.setheading(30 * hour)
    # tracer(False)
    # printer.forward(65)
    # printer.write(week(t), align="center", font=("Courier", 14, "bold"))
    # printer.back(130)
    # printer.write(date(t), align="center", font=("Courier", 14, "bold"))
    # printer.home()
    # tracer(True)
    ontimer(tick, 100)  # 100ms后继续调用tick


def main():
    tracer(False)
    # init()
    setup_clock(160)
    tracer(True)
    # tick()
    done()


main()