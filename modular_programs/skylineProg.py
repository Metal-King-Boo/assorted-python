#problem 26
#making a city skyline with turtle

import turtle
import my_graphics as mg
import random

def drawBuildings(color):
    #draw the skyline
    turtle.fillcolor(color)
    turtle.begin_fill()
    mg.line(-350, -150, -275, -150, color)
    mg.line(-275, -150, -275, 0, color)
    mg.line(-275, 0, -200, 0, color)
    mg.line(-200, 0, -200, 200, color)
    mg.line(-200, 200, 0, 200, color)
    mg.line(0, 200, 0, -50, color)
    mg.line(0, -50, 125, -50, color)
    mg.line(125, -50, 125, 100, color)
    mg.line(125, 100, 225, 100, color)
    mg.line(225, 100, 225, 0, color)
    mg.line(225, 0, 275, 0, color)
    mg.line(275, 0, 275, -150, color)
    mg.line(275, -150, 350, -150, color)

    mg.line(350, -150, 350, -300, color)
    mg.line(350, -300, -350, -300, color)
    mg.line(-350, -300, -350, -150, color)

    turtle.end_fill()

def drawWindows(color):
    #draw the windows
    mg.square(-50, 60, 30, color)
    mg.square(-180, 100, 30, color)
    mg.square(-180, 150, 30, color)
    mg.square(-90, -120, 30, color)
    mg.square(-260, -50, 30, color)
    mg.square(135, 50, 30, color)

def drawStars(color):
    #draw the stars
    for x in range(15):
        randX = random.randint(-300, 300)
        randY = random.randint(-10, 350)
        mg.circle(randX, randY, 3, color)

def main():
    turtle.hideturtle()
    turtle.bgcolor("black")
    drawStars("white")
    drawBuildings("gray")
    drawWindows("white")
    turtle.done()

main()