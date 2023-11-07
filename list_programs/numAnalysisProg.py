# problem 4
# enter a series of 20 numbers, store the list and display stats
# lowest, highest, total, and average

def main():
    numList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(20):
        userInput = float(input("Input value " + str(i + 1) + ": "))
        numList[i] = userInput

    # get the average and total
    totalValue = 0
    for x in numList:
        totalValue += x
    averageValue = totalValue / 20

    # cycle through anf compare the max value and min value
    # if max is < the current value then make that value max
    # if min is > the current value then make that value min
    maxValue = numList[0]
    minValue = numList[0]
    for y in numList:
        if (y > maxValue):
            maxValue = y
        if (y < minValue):
            minValue = y

    print("The total value:", totalValue)
    print("The data average:", averageValue)
    print("The highest value:", maxValue)
    print("The lowest value:", minValue)

main()