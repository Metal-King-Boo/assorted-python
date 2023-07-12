#question 7
#write a series of random numbers to a file

import random

def main():

    userInput = int(input("How many random numbers will be input"))

    inputFile = open("random.txt", "w")

    for i in range(userInput):
        randInput = str(random.randint(1, 500))
        inputFile.write(randInput + "\n")

    inputFile.close()

main()