# problem 2
# 7 digit lottery number put into a list then display the list

import random

def main():
    lottoList = [0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        lottoList[i] = random.randint(0,9)

    print("The 7 lotto digits are: ")
    for x in lottoList:
        print(x)

main()