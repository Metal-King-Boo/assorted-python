# Replication of the draw_squares.py program found in the textbook.

import turtle
def main():
    turtle.hideturtle()
    square(100, 0, 50, 'red')
    square(-150, -100, 200, 'blue')
    square(-200, 150, 70, 'green')

    turtle.done()

    # The square function draws a square. The x and y parameters
    # are the coordinates of the lower-left corner. The width
    # parameter is the width of each side. The color parameter
    # is the fill color, as a string.

def square(x, y, width, color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

# Call the main function.
main()