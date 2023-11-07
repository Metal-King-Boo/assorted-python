#draw several squares within each other

import turtle

#named constants
starting_distance = 20
num_squares = 100
offset = 10
animation_speed = 0

#setup turtle
turtle.speed(animation_speed)
turtle.hideturtle()
turtle.penup()
turtle.goto(325, -275)
turtle.pendown()

#set the distance to travel
distance = starting_distance

#draw the square
for count in range(num_squares):
    for x in range(4):
        turtle.back(distance)
        turtle.right(90)

    #calculate the size of the next square
    distance = distance + offset

    #position turtle for next square
    turtle.penup()
    turtle.goto(325, -275)
    turtle.pendown()

turtle.done()