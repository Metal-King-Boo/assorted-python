#draw using repeated lines

import turtle

#named constants
start_x = -200
start_y = 0
num_lines = 36
line_length = 400
angle = 170
animation_speed = 0

#move the turtle to its initial position
turtle.hideturtle()
turtle.penup()
turtle.goto(start_x, start_y)
turtle.pendown()

#set the animation speed
turtle.speed(animation_speed)

#draw 36 lines, with the turtle tilted
#by 170 degrees after each line is drawn
for x in range(num_lines):
    turtle.forward(line_length)
    turtle.left(angle)
















turtle.done()