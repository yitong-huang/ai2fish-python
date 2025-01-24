from turtle import *

def draw_polygon(n):
    for i in range(n):
        forward(100)
        right( 180 - (n-2) * 180 / n )

speed(1)
draw_polygon(8)
done()