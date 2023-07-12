# program that handles statistical data on gas prices

# function to pull the data from the file into a list
def getData():
    dataSet = []

    priceFile = open('GasPrices.txt', 'r')

    readLine = priceFile.readline()
    # read each line until there are no more in the file
    while(readLine != ''):
        # strip the line of escape keys
        stripData = readLine.strip('\n')
        # replace the remaining \'s with empty space
        replaceData = stripData.replace('\\', '')
        # split the line into "mm-dd-yyy" and "N.NNN"
        splitData = replaceData.split(':')
        # add the data to the list
        dataSet.append(splitData)
        # read the next line
        readLine = priceFile.readline()

    priceFile.close()

    # remove the last item in the list that does not have a date
    dataSet.pop()

    return dataSet

# function to get the average gas for a single year
def averagePerYear(data, year):
    total = 0;
    gas = 0;
    comparisonYear = str(year)

    for item in data:
        # this creates a string with the year value of each data record
        indexYear = item[0][6] + item[0][7] + item[0][8] + item[0][9]
        if(comparisonYear == indexYear):
            total += float(item[1])
            gas += 1

    return total / gas

# function to get the average gas for a month
def averagePerMonth(data, month, year):
    total = 0;
    gas = 0;
    comparisonYear = str(year)
    comparisonMonth = '0' + str(month)

    for item in data:
        # this creates a string with the year value of each data record
        indexYear = item[0][6] + item[0][7] + item[0][8] + item[0][9]
        # this creates a string with the month value of each data record
        indexMonth = item[0][0] + item[0][1]
        if(comparisonYear == indexYear):
            if(comparisonMonth == indexMonth):
                total += float(item[1])
                gas += 1

    # this try-except block is made to catch 0/0 for months that have no records
    try:
        average = total / gas
    except ZeroDivisionError:
        return 0

    return total / gas

# function to get the average gas for every year
def averageEveryYear(data):
    yearCounter = 1993
    # cycle through 1992 - 2012
    for i in range(21):
        average = averagePerYear(data, yearCounter)
        # print the average of each year
        print(yearCounter, "Average Gas Price:", round(average, 2))
        yearCounter += 1

# function to get the average gas for every month
def averageEveryMonth(data):
    yearCounter = 1993
    monthCounter = 1
    # cycle through 1993 - 2012
    for i in range(21):
        # cycle through the 12 months
        for monthCounter in range(1,12):
            average = averagePerMonth(data, monthCounter, yearCounter)
            # only display data if it exists in the records
            if(average > 0):
                print("0" + str(monthCounter) + "-" + str(yearCounter) + " Average Gas Price:", round(average, 2))
        yearCounter += 1

def sortLowHigh(data):
    copiedData = []

    # duplicate the data into a new list
    for item in data:
        copiedData.append(item)

    dataLength = len(copiedData)

    # cycle through the list going from index 1 to the end
    for i in range(1, dataLength):
        sortedData = copiedData[i]
        j = i - 1

        # do this as long as j is not 0 and the sortedData is less than the previous data
        while j >= 0 and float(sortedData[1]) < float(copiedData[j][1]):
            # swap the indexes to sort
            copiedData[j + 1] = copiedData[j]
            j -= 1
        #put the value of sortedData where it belongs
        copiedData[j + 1] = sortedData

    return copiedData

def sortHighLow(data):
    copiedData = []

    # duplicate the data into a new list
    for item in data:
        copiedData.append(item)

    dataLength = len(copiedData)

    # cycle through the list going from index 1 to the end
    for i in range(1, dataLength):
        sortedData = copiedData[i]
        j = i - 1

        # do this as long as j is not 0 and the sortedData is greater than the previous data
        while j >= 0 and float(sortedData[1]) > float(copiedData[j][1]):
            # swap the indexes to sort
            copiedData[j + 1] = copiedData[j]
            j -= 1
        #put the value of sortedData where it belongs
        copiedData[j + 1] = sortedData

    return copiedData

# function that takes the data and writes it to a file of your choice
def storeData(filename, data):
    openFile = open(filename, 'w')

    for item in data:
        # replace the list brackets with empty space
        lineData = str(item).replace('[', '')
        lineData = lineData.replace(']', '')
        # replace the apostrophes with empty space
        lineData = lineData.replace('\'', '')
        # replace the commas with semi-colons
        lineData = lineData.replace(',', ':')
        # write the line to file and move to the next line
        openFile.write(lineData + "\n")

    openFile.close()

def main():
    myData = getData()
    averageEveryYear(myData)
    print('--------------------------------------------')
    averageEveryMonth(myData)
    print('--------------------------------------------')
    lowHigh_myData = sortLowHigh(myData)
    storeData("GasPrices(L2H).txt", lowHigh_myData)
    print('The data has been sorted from Low to High and printed to GasPrices(L2H).txt')
    print('--------------------------------------------')
    highLow_myData = sortHighLow(myData)
    storeData("GasPrices(H2L).txt", highLow_myData)
    print('The data has been sorted from High to Low and printed to GasPrices(H2L).txt')

main()