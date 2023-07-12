# tuple problem

# this function gets the rain for each day of the week from the user
def getDailyRain(weekDays):
    rainList = []
    for i in range(7):
        rainInput = input("Enter the rainfall for " + str(weekDays[i]) +  ": ")
        rainList.append(rainInput)

    return rainList

# this function takes the rain data and gets the average for the week
def getAverageRain(rainfall):
    total = 0
    for item in rainfall:
        total += int(item)

    average = total / len(rainfall)
    return average

def main():
    weekDays = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    rainfall = getDailyRain(weekDays)
    average = getAverageRain(rainfall)

    print('--------------------')

    for i in range(7):
        print('The rainfall for', weekDays[i], 'is:', rainfall[i])
    print('The average rainfall for the week is:', average)
main()