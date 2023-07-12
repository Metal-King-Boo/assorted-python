#question 2
#display the first five lines of a a user selected file

def main():
    userFile = input("Type the name of a file to open: ")

    try:
        output = open(userFile, 'r')

        for i in range(5):
            line = output.readline()
            print(line)

        output.close()
    except IOError:
        print("file does not exist")

main()