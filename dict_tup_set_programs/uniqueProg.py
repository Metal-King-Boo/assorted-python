# unique word problem

def getData(filename):
    wordsSet = set()

    try:
        readFile = open(filename, 'r')

        readLine = readFile.readline()
        while readLine != '':
            wordsSet.update({readLine.strip()})
            readLine = readFile.readline()

        readFile.close()
    except FileNotFoundError:
        print("file does not exist")

    return wordsSet

    readFile.close()
def main():
    myData = getData('uniqueWordsList.txt')

    print("All Unique Entries in the List:")
    for item in myData:
        print(item)
main()