#draw a star shape using lines and loops

import turtle

#named constants
start_x = -200
start_y = 0
num_lines = 8
line_length = 400
angle = 225
animation_speed = 0

#setup turtle
turtle.hideturtle()
turtle.penup()
turtle.goto(start_x, start_y)
turtle.pendown()
turtle.speed(animation_speed)

#draw 8 lines with turtle titled
#by 45 degrees after each line is drawn
for x in range(num_lines):
    turtle.forward(line_length)
    turtle.left(angle)

turtle.done()