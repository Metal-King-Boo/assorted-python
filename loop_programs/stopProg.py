#making a stop sign in turtle

import turtle

#named constants
animation_speed = 0

#setup turtle
turtle.speed(animation_speed)
turtle.hideturtle()
turtle.penup()
turtle.goto(-50, 125)
turtle.pendown()

#fill the octogon with red
turtle.fillcolor('red')
turtle.begin_fill()

#draw the octogon
for x in range(8):
    turtle.forward(100)
    turtle.right(45)

#stop coloring the octogon
turtle.end_fill()

#write STOP on the stop sign
turtle.penup()
turtle.goto(-10, 0)
turtle.pendown()
turtle.write("STOP")

turtle.done()