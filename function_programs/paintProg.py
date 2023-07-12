#paint job program for calculating the cost of a paint job
import math

#this function calculates the gallons of paint required and the total paint cost
def paintMath(wall, paint):
    #rounds up since you will need to buy an entire gallon even if you need a little more
    gallAmount = math.ceil(wall / 112)
    print("Gallons of paint required: ", gallAmount)

    #converts the gallons needed into an actual price based on the value the user gave
    paintPrice = gallAmount * paint
    print("Total paint cost: $", paintPrice)
    return paintPrice

#this function calculated the amount of hours worked and the total labor cost
def laborMath(wall):
    #rounds up since you pay them for the whole hour even if they are 5 minutes early
    #you dont want to undercut someone's pay
    #112ft for 8hrs is 14ft for 1hr
    hoursWorked = math.ceil(wall / 14)
    hoursWorked = hoursWorked * 1
    print("Hours worked: ", hoursWorked)

    #turns the worked hours into their paycheck of $35 an hour
    labor = hoursWorked * 35
    print("Total labor cost: $", labor)
    return labor

#main function to run the program
def main():
    #get the user's input on the program
    wall = int(input("How many square feet of walls will be painted? "))
    paint = int(input("How much is 1 gallon of your paint cost? "))
    print()

    #run the previously defined functions
    paintPrice = paintMath(wall, paint)
    labor = laborMath(wall)

    #get the total cost at the end and print it
    totalCost = paintPrice + labor
    print("Your total cost is $", totalCost)

#call the main function
main()