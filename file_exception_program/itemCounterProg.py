#question 4
#get the number of names in a a file named "names.txt"

def main():

    try:
        output = open('names.txt', 'r')

        line = output.readline()
        nameCount = 0

        while line != '':
            line = output.readline()
            nameCount += 1

        print("There are " + str(nameCount) + " names in the file")

        output.close()
    except IOError:
        print("file does not exist")

main()