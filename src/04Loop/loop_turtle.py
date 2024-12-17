import turtle


turtleSpeed = 1
distance = 200.0
angle = 90

turtle.speed(turtleSpeed)

# turtle.forward(distance)
# turtle.left(angle)
# turtle.forward(distance)
# turtle.left(angle)
# turtle.forward(distance)
# turtle.left(angle)
# turtle.forward(distance)
# turtle.left(angle)

i = 0
while i < 4:
    turtle.forward(distance)
    turtle.left(angle)
    i += 1  # i = i + 1


turtle.mainloop()
