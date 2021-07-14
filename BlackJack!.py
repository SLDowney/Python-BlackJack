import random
import db as db

def getPlayerBet(playerMoney):
    maxBet = db.readPlayerMoney()
    playerMoney = float(playerMoney)
    print("\nMoney: ", maxBet)
    print()
    
    while True:
        try:
            betAmount = float(input("Bet Amount: "))
            if (betAmount >= 5 and betAmount <= 1000) and betAmount <= float(maxBet):
                playerMoney = playerMoney - betAmount
                db.writePlayerMoney(playerMoney)
                print()
                return betAmount
            elif betAmount < 5 or betAmount > 1000 or betAmount > playerMoney:
                print("Invalid bet amount. Bets must be between 5 and 1000, and can't be less than your current balance, $" + str(playerMoney) + ".\n")
                continue
        except ValueError:
            print("Please enter a valid number.\n")
            continue
        return playerMoney

def playerWins(playerMoney, betAmount):
    winnings = betAmount * 1.5
    playerMoney = float(playerMoney) + winnings
    db.writePlayerMoney(playerMoney)
    print("\nMONEY :", db.readPlayerMoney())
    return playerMoney

def playerLoss(playerMoney, betAmount):
    playerMoney = float(playerMoney)
    db.writePlayerMoney(playerMoney)
    print("\nMONEY: ", db.readPlayerMoney())
    if playerMoney < 5:
        buyMore = input("Balance less than minimum bet, would you like to top up to $100? (y/n): ")
        if buyMore.lower() == "y":
            playerMoney = 100

    
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
    print("Shuffling deck...\n")

def getPlayerCards(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1):
    playerCard = random.choice(cards)
    playerCards.append(playerCard)
    cards.remove(playerCard)
    if playerCard[1] == "Ace":
        playerCheckForAce(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1)
    return playerCard

def getDealerCards(cards, dealerCards):
    dealerCard = random.choice(cards)
    dealerCards.append(dealerCard)
    cards.remove(dealerCard)
    return dealerCard

def playerHand(playerCards):
    for card in playerCards:
        suit = card[0]
        face = card[1]
        print(str(face) + " of " + str(suit))

def dealerHand(dealerCards):
    for card in dealerCards:
        suit = card[0]
        face = card[1]
        print(str(face) + " of " + str(suit))

def DealCards(dCard1, playerCards, dealerCards, playerMoney, betAmount, cards):

    print("DEALER'S SHOW CARD: ")
    print(dCard1[1], " of ", dCard1[0])
    print("DEALER POINTS: ", dCard1[2])
    
    print("\nYOUR CARDS: ")
    pCard1 = getPlayerCards(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1)
    pCard2 = getPlayerCards(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1)
    playerHand(playerCards)
    print("PLAYER POINTS: ", playerPoints(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1))

def playerTurnHit(cards, playerCards, dealerCards, playerMoney, betAmount, dCard1):
    pHitCard = getPlayerCards(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1)
    playerHand(playerCards)
    print("PLAYER POINTS: ", playerPoints(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1))
    return pHitCard

def playerTurnStand(cards, dealerCards, dCard1, dCard2, playerCards, playerMoney, betAmount, totalPlayerPoints):
    dealerTurnHit(cards, dealerCards, playerCards, playerMoney, betAmount, totalPlayerPoints)

def playerCheckForAce(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1):
    totalPlayerPoints = playerPoints(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1)
    if totalPlayerPoints > 21:
        for card in playerCards:
            if card[1] == "Ace":
                card[2] == 1
                playerPoints(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1)
            else:
                playerLoss(playerMoney, betAmount)

def dealerCheckForAce(dealerCards, playerCards, playerMoney, betAmount, cards, dCard1):
    for card in dealerCards:
        if card[1] == "Ace":
            card[2] == 1
            dealerPoints(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1)

def getPlayerPoints():
    pass

def playerPoints(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1):
    totalPlayerPoints = 0
    for card in playerCards:
        values = card[2]
        totalPlayerPoints = totalPlayerPoints + values
    
    while totalPlayerPoints == 21 or totalPlayerPoints > 21:
        if totalPlayerPoints == 21:
            playerWins(playerMoney, betAmount)
        elif totalPlayerPoints > 21:
            checkWinner(playerCards, dealerCards, playerMoney, betAmount, cards, totalPlayerPoints, dCard1)
            return totalPlayerPoints
    return totalPlayerPoints
    
def dealerPoints(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1):
    totalDealerPoints = 0
    for card in dealerCards:
        values = int(card[2])
        totalDealerPoints += values
    
    while totalDealerPoints == 21 or totalDealerPoints > 21:
        if totalDealerPoints == 21:
            playerLoss(playerMoney, betAmount)
            exit()
        elif totalDealerPoints > 21:
            dealerCheckForAce(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1)
            break
    return totalDealerPoints

def dealerTurnHit(cards, dealerCards, playerCards, playerMoney, betAmount, totalPlayerPoints, dCard1):
    print("\nDEALER's CARDS: ")
    dealerHand(dealerCards)
    print("DEALER POINTS: ", dealerPoints(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1), "\n")

    while dealerPoints(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1) < 17:
        print("\nDealer hits...\n")
        dCard3 = getDealerCards(cards, dealerCards)
        print(dCard3[1], " of ", dCard3[0])
        print("\nDEALER POINTS: ", dealerPoints(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1))
    
    checkWinner(playerCards, dealerCards, playerMoney, betAmount, cards, totalPlayerPoints, dCard1)

def checkWinner(playerCards, dealerCards, playerMoney, betAmount, cards, totalPlayerPoints, dCard1):

    totalDealerPoints = dealerPoints(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1)
    #while True:
    if totalPlayerPoints > 21:
        for card in playerCards:
            #values = card[2]
            if card[2] == 11:
                card[2] = 1
                totalPlayerPoints -= 10
        print("PLAYER POINTS: ", totalPlayerPoints)
        print("\nPLAYER BUST!! HA HA SUCKS TO BE YOU")
        playerLoss(playerMoney, betAmount)
        return False
    elif totalPlayerPoints == 21:
        print("\nBLACKJACK !!! You must have cheated, you're not THAT good...")
        playerWins(playerMoney, betAmount)
        return False
    elif totalPlayerPoints < 21:
        if totalDealerPoints > 21:
                print("\nDEALER LOSES, VICTORY!")
                playerWins(playerMoney, betAmount)
                return False
        elif totalDealerPoints == 21:
            print("\nDEALER BLACKJACK!! DEALER WINS!")
            playerLoss(playerMoney, betAmount)
            return False
        elif totalDealerPoints < 21:
            if totalPlayerPoints > totalDealerPoints:
                print("\nPLAYER WINS!!")
                playerWins(playerMoney, betAmount)
                return False
            elif totalPlayerPoints == totalDealerPoints:
                print("\nIT'S A DRAW!")
                return False
            else:
                print("\nYOU LOSE SUCKER !")
                playerLoss(playerMoney, betAmount)
                return False

    #Round payout to max 2 decimal places

def hitStand(cards, dealerCards, playerCards, playerMoney, betAmount, totalPlayerPoints, dCard1):
    playerChoice = input("\nHit or Stand? >> ")
    if playerChoice.lower() == "hit":
        playerTurnHit(cards, playerCards, dealerCards, playerMoney, betAmount, dCard1)
    elif playerChoice.lower() == "stand":
        dealerTurnHit(cards, dealerCards, playerCards, playerMoney, betAmount, totalPlayerPoints, dCard1)
    else:
        print("Please enter a valid command.")

def main():
    
    playerMoney = db.startingPlayerMoney()
    db.writePlayerMoney(playerMoney)

    print("BLACKJACK!")
    print("Blackjack payout os 3:2\n")
    
    keepGoing = "y"
    while keepGoing.lower() == "y":
        betAmount = getPlayerBet(playerMoney)
        playerMoney = db.readPlayerMoney()
        
        cards = cardDeck()
        
        shuffleDeck(cards)
        
        playerCards = []
        dealerCards = []
        pCard1 = 0
        pCard2 = 0
        dCard1 = 0
        dCard2 = 0
        
        dCard1 = getDealerCards(cards, dealerCards)
        dCard2 = getDealerCards(cards, dealerCards)

        DealCards(dCard1, playerCards, dealerCards,playerMoney, betAmount, cards)

        totalPlayerPoints = playerPoints(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1)
        totalDealerPoints = dealerPoints(playerCards, dealerCards, playerMoney, betAmount, cards, dCard1)

        
        while totalPlayerPoints < 21 and totalDealerPoints < 21:
            hitStand(cards, dealerCards, playerCards, playerMoney, betAmount, totalPlayerPoints, dCard1)
            totalPlayerPoints
        if totalPlayerPoints > 21 or totalDealerPoints > 21:
            checkWinner(playerCards, dealerCards, playerMoney, betAmount, cards, totalPlayerPoints, dCard1)
    
        keepGoing = input("\nPlay Again? (y/n): ")
    
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
