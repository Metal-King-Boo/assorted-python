# collect user name and date of birth
# convert date of birth to current age
# display name, age, and today's date
from datetime import date

#user input
name = input("What is your name? ")
dateM = input("What month were you born? (mm) ")
dateD = input("What day were you born? (dd) ")
dateY = input("What year were you born? (yyyy) ")

#collecting dates
now = date.today()
dateBirth = date(int(dateY), int(dateM), int(dateD))

#calculating current age
ageCalc = (now.month) < (dateBirth.month) and (now.day) < (dateBirth.day)
newAge = now.year - dateBirth.year - 1 + ageCalc

#output
print("-----------------")
print("Today's Date: " + str(now))
print("Your name: " + name)
print("Your current age: " + str(newAge))