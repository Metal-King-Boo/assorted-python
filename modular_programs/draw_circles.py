# Replication of the draw_circles.py program found in the textbook.

import turtle

def main():
    turtle.hideturtle()
    circle(0, 0, 100, 'red')
    circle(-150, -75, 50, 'blue')
    circle(-200, 150, 75, 'green')

    turtle.done()

    # The circle finction draws a circle. The x and y parameters
    # are the coordinates of the center point. The radius
    # parameter is the circle's radius. The color parameter
    # is the fill color, as a string.

def circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Call the main function.
main()