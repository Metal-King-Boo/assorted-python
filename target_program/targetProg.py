#based on hit_the_target.py
# user inputs angle and launch force to try and hit a target
import turtle

#named constants
#screen size
screen_width = 600
screen_height = 600
#target parameters
target_lleft_x = 100
target_lleft_y = 250
target_width = 25
#vector values
force_factor = 30
projectile_speed = 1
#angles
north = 90
south = 270
east = 0
west = 180

#window setup
turtle.setup(screen_width, screen_height)

#draw the target
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(target_lleft_x, target_lleft_y)
turtle.pendown()
#set direction and draw
turtle.setheading(east)
turtle.forward(target_width)
#change directions to north
turtle.setheading(north)
turtle.forward(target_width)
#change directions to west
turtle.setheading(west)
turtle.forward(target_width)
#change directions to south
turtle.setheading(south)
turtle.forward(target_width)
turtle.penup()

#center the turtle
turtle.goto(0, 0)
turtle.setheading(east)
turtle.showturtle()
turtle.speed(projectile_speed)

#get the angle and force from user
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1-10): "))

#calculate the distance
distance = force * force_factor

#set the heading
turtle.setheading(angle)

#launch the projectile
turtle.pendown()
turtle.forward(distance)

#did you hit the target?
#if the x and y coordinates are both found within the target space you hit it
if  (turtle.xcor() >= target_lleft_x and
     turtle.xcor() <= (target_lleft_x + target_width) and
     turtle.ycor() >= target_lleft_y and
     turtle.ycor() <= (target_lleft_y + target_width)):
        print("Target Hit!")
#if the any of coordinates are not found within the target space then you missed
else:
        print("You missed the target.")

