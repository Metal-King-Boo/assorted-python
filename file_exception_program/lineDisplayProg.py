#question 3
#display a line number for every line transcribed

def main():
    userFile = input("Type the name of a file to open: ")

    try:
        output = open(userFile, 'r')

        lineCount = 1
        line = output.readline()

        while line != '':
            print(str(lineCount) + ": " + line)
            line = output.readline()
            lineCount += 1

        output.close()
    except IOError:
        print("file does not exist")

main()