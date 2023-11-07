# problem 10
# world championship baseball teams menu

# create a list with the raw data from the file
def getData(filename):
    rawData = []
    try:
        readFile = open(filename, "r")

        readLine = readFile.readline()
        readLine = readLine.rstrip("\n")

        while (readLine != ""):
            rawData.append(readLine)
            readLine = readFile.readline()
            readLine = readLine.rstrip("\n")

        readFile.close()
    except IOError:
        print("That file does not exist")
    except:
        print("An error has occured")


    return rawData

# create a list of unique teams
def setMenu(data):
    teams = []
    for item in data:
        unique = True
        for i in teams:
            if item == i:
                unique = False
        if unique == True:
            teams.append(item)

    return teams

# create a display of all the unique teams to select from
def displayMenu(teams):
    counter = 1
    for team in teams:
        print(counter, ": ", team)
        counter += 1
    choice = int(input("Enter your team ID: "))
    return choice

# get the amount of times a particular team has won
def howManyWins(option, data, menu):
    numberOfWins = 0

    # take the user selection and change it into the team name
    if option > 28 or option < 1:
        print("Invalid team ID")
        exit()
    else:
        name = menu[option - 1]
        print(option, "|", name)

        for item in data:
            if (item == name):
                numberOfWins += 1

    return numberOfWins

def main():

    myData = getData("WorldSeriesWinners.txt")
    myMenu = setMenu(myData)
    option = displayMenu(myMenu)
    print("This team has won:", howManyWins(option, myData, myMenu), "times")

main()