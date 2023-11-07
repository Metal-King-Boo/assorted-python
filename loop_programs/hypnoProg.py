#draw a blocky hypno swirl with turtle

import turtle

#named constants
starting_distance = 20
num_turns = 100
offset = 10
animation_speed = 0

#setup turtle
turtle.speed(animation_speed)
turtle.hideturtle()
turtle.penup()
turtle.goto(10, 0)
turtle.pendown()

#set travel distance
distance = starting_distance

#draw the hypo spiral
for count in range(num_turns):
    turtle.left(90)
    turtle.forward(distance)
    distance = distance + offset

turtle.done()