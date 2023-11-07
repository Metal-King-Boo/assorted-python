#drawing using repeated circles

import turtle

#named constants
num_circles = 36
radius = 100
angle = 10
animation_speed = 0

#set the animation speed
turtle.speed(animation_speed)

#draw 36 circles, with the turtle tilted
#by 10 degrees after each circle is drawn
for x in range(num_circles):
    turtle.circle(radius)
    turtle.left(angle)

turtle.done()