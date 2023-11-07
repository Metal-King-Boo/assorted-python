#rainProg
#program to calculate average rainfall within a given time period

years = input("How many years are being recorded? ")
#primer for the outer while loop
yearsCounter = int(years)
#primer for the inner while loop
monthsCounter = 0
#int for storing the rain values
rainList = 0
#int for storing the amount of times a record is recorded
rainDividend = yearsCounter * 12

while yearsCounter > 0:
    #space to break between the years on loop
    print()
    while monthsCounter < 12:
        rainInput = int(input("How much rain has fallen this month? "))
        #adds the rain input into the total rain value
        rainList += rainInput
        #raise the counter so the inner loop is not infinite
        monthsCounter += 1
    #lower the counter so the outer loop is not infinite
    yearsCounter -= 1
    #reset the months counter so it works normally on the second pass
    monthsCounter = 0

#calculate the average of the total rain data
averageRain = rainList / rainDividend
print("Total rain in " + years + " year(s) is ", averageRain)