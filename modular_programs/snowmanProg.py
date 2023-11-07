#problem 23
#making a snowman with turtle

import turtle
import my_graphics as mg

def drawBase():
    #draw the legs
    mg.circle(0, -100, 100, "white")

def drawMidSection():
    #draw the torso
    mg.circle(0, 74, 75, "white")

def drawArms():
    #draw the left arm
    mg.line(-75, 74, -125, 80, "black")
    mg.line(-125, 80, -135, 120, "black")
    mg.line(-135, 120, -115, 130, "black")
    mg.line(-135, 120, -155, 125, "black")

    #draw the right arm,
    mg.line(75, 74, 140, 100, "black")
    mg.line(140, 100, 150, 120, "black")
    mg.line(140, 100, 160, 90, "black")


def drawHead():
    #draw the head
    mg.circle(0, 200, 50, "white")

    #draw the face
    mg.circle(-17, 200, 7, "white")
    mg.circle(17, 200, 7, "white")
    mg.line(-30, 180, 30, 180, "black")

def drawHat():
    # draw the hat
    turtle.fillcolor("black")
    turtle.begin_fill()
    mg.line(0, 220, -75, 220, "black")
    mg.line(-75, 220, -75, 245, "black")
    mg.line(-75, 245, 75, 245, "black")
    mg.line(75, 245, 75, 220, "black")
    mg.line(75, 220, 0, 220, "black")
    turtle.end_fill()
    mg.square(-29, 230, 60, "black")

def main():
    turtle.hideturtle()
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()
    turtle.done()

main()