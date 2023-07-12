#question 1
#display all the numbers in a file

def main():
    output = open('numbers.txt', 'r')

    line = output.readline()

    while line != '':
        amount = float(line)
        print(amount)
        line = output.readline()
        
    output.close()

main()