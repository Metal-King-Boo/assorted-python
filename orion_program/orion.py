#program replicating orion.py in the textbook
#it draws the Orion Constellation using Turtle Graphics
import turtle

#intialize turtle
turtle.setup(500, 600)
turtle.penup()
turtle.hideturtle()

#setup the star coordinates
shoulderLX = -70
shoulderLY = 200

shoulderRX = 80
shoulderRY = 180

beltLX = -40
beltLY = -20

beltMX = 0
beltMY = 0

beltRX = 40
beltRY = 20

kneeLX = -90
kneeLY = -180

kneeRX = 120
kneeRY = -140

#draw the stars on the turtle canvas
turtle.goto(shoulderLX, shoulderLY)
turtle.dot()

turtle.goto(shoulderRX, shoulderRY)
turtle.dot()

turtle.goto(beltLX, beltLY)
turtle.dot()

turtle.goto(beltMX, beltMY)
turtle.dot()

turtle.goto(beltRX, beltRY)
turtle.dot()

turtle.goto(kneeLX, kneeLY)
turtle.dot()

turtle.goto(kneeRX, kneeRY)
turtle.dot()

#display the names of each star
turtle.goto(shoulderLX, shoulderLY)
turtle.write('Betelgeuse')

turtle.goto(shoulderRX, shoulderRY)
turtle.write('Meissa')

turtle.goto(beltLX, beltLY)
turtle.write('Alnitak')

turtle.goto(beltMX, beltMY)
turtle.write('Alnilam')

turtle.goto(beltRX, beltRY)
turtle.write('Mintaka')

turtle.goto(kneeLX, kneeLY)
turtle.write('Saiph')

turtle.goto(kneeRX, kneeRY)
turtle.write('Rigel')

#draw connecting lines into a visible constellation
#left shoulder to left belt
turtle.goto(shoulderLX, shoulderLY)
turtle.pendown()
turtle.goto(beltLX, beltLY)
turtle.penup()

#right shoulder to right belt
turtle.goto(shoulderRX, shoulderRY)
turtle.pendown()
turtle.goto(beltRX, beltRY)
turtle.penup()

#left belt to middle belt
turtle.goto(beltLX, beltLY)
turtle.pendown()
turtle.goto(beltMX, beltMY)
turtle.penup()

#middle belt to right belt
turtle.goto(beltMX, beltMY)
turtle.pendown()
turtle.goto(beltRX, beltRY)
turtle.penup()

#left belt to left knee
turtle.goto(beltLX, beltLY)
turtle.pendown()
turtle.goto(kneeLX, kneeLY)
turtle.penup()

#right belt to right knee
turtle.goto(beltRX, beltRY)
turtle.pendown()
turtle.goto(kneeRX, kneeRY)
turtle.penup()

#keep the window open
turtle.done()

