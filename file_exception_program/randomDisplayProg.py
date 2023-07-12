#question 8
#read the random.txt file and give some basic statistics

def main():

    try:
        output = open('random.txt', 'r')

        line = output.readline()
        sum = 0
        numRead = 0

        while line != '':
            numRead += 1
            amount = float(line)
            sum += amount
            line = output.readline()

        print("The sum of random.txt is " + str(sum))
        print("The number of random integers read is " + str(numRead))

        output.close()
    except IOError:
        print("file does not exist")

main()