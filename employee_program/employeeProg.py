# problem 4

# class that holds employee information
class Employee:

    def __init__(self, name, employID, department, title):
        self.name = name
        self.employID = employID
        self.department = department
        self.title = title

    def getInformation(self):
        information = self.name + "\t" + str(self.employID) + "\t" + self.department + "\t" + self.title
        return information

# method that takes the input data and stores it to file
def saveToFile(filename, employ):

    employFile = open(filename, 'w')

    for item in employ:
        employFile.writelines(item.getInformation() + "\n")

    employFile.close()

# method that adds employees to the list
def addEmployees():
    employeeList = []
    choice = 'Y'
    while choice == 'Y' or choice == 'y':
        employee_name = input("Enter the Employee\'s Name: ")
        employee_id = input("Enter the Employee\'s ID: ")
        employee_department = input("Enter the Employee\'s Department: ")
        employee_title = input("Enter the Employee\'s Title: ")

        newEmployee = Employee(employee_name, employee_id, employee_department, employee_title)
        employeeList.append(newEmployee)

        print('---------------------------------------')
        choice = input('Add another employee? (Y/N) ')
        print('---------------------------------------')

    return employeeList

def main():

    # test information for the program
    # Name          ID     Department     Job Title
    # Susan Meyers  47899  Accounting     Vice President
    # Mark Jones    39119  IT             Programmer
    # Joy Rogers    81774  Manufacturing  Engineer)

    myEmployees = addEmployees()

    # display the information to the console
    print("Name \tEmployeeID \tDepartment \tJob Title")
    for item in myEmployees:
        print(item.getInformation())

    # ask the user whether they want it saved as a file
    print('---------------------------------------')
    fileSelection = input("Would you like to save this as a file? (Y/N) ")

    if(fileSelection == 'Y' or fileSelection == 'y'):
        saveToFile('employeeList.txt', myEmployees)
        print('File has been saved.')
main()