#question 6
#get the avearage of all the numbers in numbers.txt

def main():

    try:
        output = open('numbers.txt', 'r')

        line = output.readline()
        sum = 0
        dividend = 0

        while line != '':
            dividend += 1
            amount = float(line)
            sum += amount
            line = output.readline()

        average = sum / dividend
        print("The average of numbers.txt is " + str(average))

        output.close()
    except IOError:
        print("file does not exist")

main()