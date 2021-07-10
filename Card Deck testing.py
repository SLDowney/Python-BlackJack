import random

def startingPlayerMoney():
    try:
        playerMoney = [100]
        with open("money.txt", "w") as file:
            file.write(str(playerMoney))
        return playerMoney
    except FileNotFoundError:
        print("Error in starting Player Money function! Line 10")

def writePlayerMoney(playerMoney):
    try:
        with open("money.txt", "w") as file:
            file.write(str(playerMoney) + "\n")
        return playerMoney
    except FileNotFoundError:
        print("Error in Write Player Money Function! Line 18")

def getPlayerBet(playerMoney):
    print("Money: ", playerMoney[0])
    betAmount = float(input("Bet Amount: "))
    print()
    try:
        playerMoney = playerMoney[0] - betAmount
        with open("money.txt", "w") as file:
            file.write(str(playerMoney) + "\n")
        return playerMoney
    except ValueError:
        print("Value Error Line 31, please try again!")
        return betAmount
    #get either float or int for bet amount

def cardDeck():
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    cardDeck = []
    for suit in suits:
        i = 0
        for face in faces:
            cards = []
            cards.append(suit)
            cards.append(face)
            cards.append(values[i])
            cardDeck.append(cards)
            i = i + 1
    return cardDeck

def shuffleDeck(cards):
    random.shuffle(cards)
    print("DECK SUCCESSFULLY SHUFFLED !! Line 51")

def getPlayerCards(cards, playerCards):
    playerCard = random.choice(cards)
    playerCards.append(playerCard)
    cards.remove(playerCard)
    return playerCard

def getDealerCards(cards, dealerCards):
    dealerCards = random.choice(cards)
    dealerCards.append(dealerCards)
    cards.remove(dealerCards)
    return dealerCards

def DealCards(pCard1, pCard2, dCard1):

    print("DEALER'S SHOW CARD: ")
    print(dCard1[1], " of ", dCard1[0] + "\n")
    
    print("YOUR CARDS: ")
    print(pCard1[1], " of ", pCard1[0])
    print(pCard2[1], " of ", pCard2[0])

def playerTurnHit(cards, playerCards, pCard1, pCard2):
    pHitCard = getPlayerCards(cards, playerCards)
    
    print("YOUR CARDS: ")
    print(pCard1[1], " of ", pCard1[0])
    print(pCard2[1], " of ", pCard2[0])
    print(pHitCard[1], " of ", pHitCard[0])
    return pHitCard


def playerTurnStand():
    print("Entered the playerTurnStand function!")

def playerPoints():
    pass

def dealerPoints():
    pass

def checkWinner():
    pass
    #Round payout to max 2 decimal places

def main():
    
    playerMoney = startingPlayerMoney()
    savePlayerMoney = writePlayerMoney(playerMoney)

    print("BLACKJACK!")
    print("Blackjack payout os 3:2\n")
    
    getPlayerBet(playerMoney)
    
    cards = cardDeck()

    playerCards = []
    dealerCards = []
    
    pCard1 = getPlayerCards(cards, playerCards)
    pCard2 = getPlayerCards(cards, playerCards)
    dCard1 = getDealerCards(cards, dealerCards)
    dCard2 = getDealerCards(cards, dealerCards)

    DealCards(pCard1, pCard2, dCard1)

    playerChoice = input("\nHit or Stand?: ")
    if playerChoice.lower() == "hit":
        playerTurnHit(cards, playerCards, pCard1, pCard2)
    elif playerChoice.lower() == "stand":
        playerTurnStand()
    else:
        print("Error Line 127")



if __name__ == "__main__":
    main()