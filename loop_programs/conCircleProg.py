#concentric circles draw

import turtle

#named constants
num_circles = 20
starting_radius = 20
offset = 10
animation_speed = 0

#setup turtle
turtle.speed(animation_speed)
turtle.hideturtle()

#set the radius of the first circle
radius = starting_radius

#draw the circle
for count in range(num_circles):
    #draw the circle.
    turtle.circle(radius)

    #get the coordinates for the next circle
    x = turtle.xcor()
    y = turtle.ycor() - offset

    #calculate the radius for the next circle
    radius = radius + offset

    #position the turtle for the next circle
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.done()