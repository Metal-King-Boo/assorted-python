# question 14
# pie chart that shows how much money you are spending for the last month

import matplotlib.pyplot as pit

# opens the file 'monthlyexpenses.txt' and copies data from it
def getData():
    dataSet = []

    try:
        audit = open('monthlyexpenses.txt', 'r')

        readLine = audit.readline()
        # repeat until there are no more lines of in the file to be read
        while(readLine != ""):
            # strip the data of its escape key
            new_input_no_escape = readLine.strip('\n')
            # split the string into "category:" and "$DDD.CC"
            category_prices_list = new_input_no_escape.split()
            # strip the pricing string of its dollar sign
            pricing = category_prices_list[len(category_prices_list) - 1].strip('$')
            # add the value to the data set
            dataSet.append(pricing)
            # get the next line
            readLine = audit.readline()

        audit.close()

    except FileNotFoundError:
        print('File could not be found')

    return dataSet

# converts the list of strings into a list of floats
def convertData(myData):
    dataSet = []

    for item in myData:
        dataSet.append(float(item))

    return dataSet

def main():

    # create list and labels
    myData = getData()
    data = convertData(myData)
    expense_labels = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']

    # input the data and title then display it
    pit.pie(data, labels=expense_labels)
    pit.title('Last Month\'s Expenses')
    pit.show()

main()