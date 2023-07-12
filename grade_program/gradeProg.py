#gradeProg.py
#This program will return a grade letter based on the number given

#declare the variables and gain user input
userGrade = input("Enter the grade number (0-100): ")

#turn the string input into an int for comparison reasons
userGrade = int(userGrade)

#if statement to determine the matching letter for the grade given
#if the number is higher than 100, print an error
if(userGrade > 100):
    print("Error: input is not between 0 and 100")
#if the number is lower than 100 but higher than 89, print A
elif(userGrade >= 90):
    print("A")
#if the number is lower than 90 but higher than 79, print B
elif(userGrade >= 80):
    print("B")
#if the number is lower than 80 but higher than 69, print C
elif(userGrade >= 70):
    print("C")
#if the number is lower than 60 but higher than 59, print D
elif(userGrade >= 60):
    print("D")
#if the number is lower than 50 but higher than 0, print E
elif(userGrade >= 0):
    print("E")
#if the number is lower than 0, print an error
else:
    print("Error, input is not between 0 and 100")