#program that sets up a game of rock paper scissors for the user
import random

#function that sets up the bot's hand
def rpsHand():
    bot = random.randint(1, 3)
    if(bot == 1):
        hand = 'Rock'
    elif(bot == 2):
        hand = 'Paper'
    else:
        hand = 'Scissors'

    return hand

#function that decides the winner based on both hands
def results(playerHand, botHand):
    #if the hands are the same tie
    if(playerHand == botHand):
        result = 'Tie'
    #the outcomes if player chooses Rock
    elif(playerHand == 'Rock' and botHand == 'Paper'):
        result = 'Victory!'
    elif(playerHand == 'Rock' and botHand == 'Scissors'):
        result = 'Defeated...'
    #the outcomes if the player chooses Paper
    elif (playerHand == 'Paper' and botHand == 'Rock'):
        result = 'Victory!'
    elif (playerHand == 'Paper' and botHand == 'Scissors'):
        result = 'Defeated...'
    #the outcomes if the player chooses Scissors
    elif (playerHand == 'Scissors' and botHand == 'Paper'):
        result = 'Victory!'
    elif (playerHand == 'Scissors' and botHand == 'Rock'):
        result = 'Defeated...'
    #the outcomes if the player chooses gibberish or illegal hands
    else:
        result = 'Illegal Player hand'

    return result

def main():
    botHand = rpsHand()

    playerHand = input("Enter \"Rock\", \"Paper\", or \"Scissors\": ")
    print("Your Opponent has chosen: ", botHand)

    result = results(playerHand, botHand)
    print(result)

main()


