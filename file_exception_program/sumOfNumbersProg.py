#question 5
#get the sum of the numbers found in numbers.txt

def main():

    try:
        output = open('numbers.txt', 'r')

        line = output.readline()
        sum = 0

        while line != '':
            amount = float(line)
            sum += amount
            line = output.readline()

        print("The sum of numbers.txt is " + str(sum))

        output.close()
    except IOError:
        print("file does not exist")

main()