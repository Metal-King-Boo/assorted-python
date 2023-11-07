# problem 3
# monthly rainfall for a year, get the average, get the highest and lowest

def main():
    rainList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(12):
        monthlyRain = float(input("Input Month " +  str(i + 1) + "\'s rainfall: "))
        rainList[i] = monthlyRain

    # get the average rain
    totalRain = 0
    for x in rainList:
        totalRain += x
    averageRain = totalRain / 12

    # cycle through anf compare the max rain and min rain
    # if max is < the current value then make that value max
    # if min is > the current value then make that value min
    maxRain = rainList[0]
    minRain = rainList[0]
    for y in rainList:
        if(y > maxRain):
            maxRain = y
        if(y < minRain):
            minRain = y

    print("The average rainfall:", averageRain)
    print("The highest amount of rainfall:", maxRain)
    print("The lowest amount of rainfall:", minRain)

main()