import random
import db as db

def getPlayerBet(playerMoney):
    print("Money: ", playerMoney[0])
    print()
    
    while True:
        try:
            betAmount = float(input("Bet Amount: "))
            if (betAmount >= 5 and betAmount <= 1000) and betAmount <= playerMoney[0]:
                playerMoney = playerMoney[0] - betAmount
                with open("money.txt", "w") as file:
                    file.write(str(playerMoney) + "\n")
                print()
                return betAmount
            elif betAmount < 5 or betAmount > 1000 or betAmount > playerMoney[0]:
                print("Invalid bet amount. Bets must be between 5 and 1000, and can't be less than your current balance, $" + str(playerMoney[0]) + ".\n")
                continue
        except ValueError:
            print("Please enter a valid number.\n")
            continue

def playerWins(playerMoney, betAmount):
    winnings = betAmount * 1.5
    playerMoney = playerMoney + winnings
    db.writePlayerMoney(playerMoney)
    return playerMoney

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
    dealerCard = random.choice(cards)
    dealerCards.append(dealerCard)
    cards.remove(dealerCard)
    return dealerCard

def DealCards(pCard1, pCard2, dCard1, playerCards):

    print("DEALER'S SHOW CARD: ")
    print(dCard1[1], " of ", dCard1[0])
    print("DEALER POINTS: ", dCard1[2])
    
    print("\nYOUR CARDS: ")
    print(pCard1[1], " of ", pCard1[0])
    print(pCard2[1], " of ", pCard2[0])
    print("PLAYER POINTS: ", playerPoints(playerCards))

def playerTurnHit(cards, playerCards):
    pHitCard = getPlayerCards(cards, playerCards)
    for card in playerCards:
        print(card[1], " of ", card[0])
    print("PLAYER POINTS: ", playerPoints(playerCards))
    return pHitCard

def playerTurnStand(cards, dealerCards, dCard1, dCard2, playerCards, playerMoney, betAmount):
    dealerTurnHit(cards, dealerCards, dCard1, dCard2, playerCards, playerMoney, betAmount)

def playerPoints(playerCards, dealerCards, playerMoney):
    totalPlayerPoints = 0
    for card in playerCards:
        values = card[2]
        totalPlayerPoints = totalPlayerPoints + values
        if totalPlayerPoints == 21:
            print("PLAYER POINTS: ", totalPlayerPoints, "\nBLACKJACK !!!")
            exit()
        elif totalPlayerPoints > 21:
                    for card in playerCards:
                        if card[0] == "Ace":
                            card[2] == 1
                            playerPoints(playerCards)
                        else:
                            checkWinner(playerCards, dealerCards, playerMoney)
    return totalPlayerPoints
    
def dealerPoints(dealerCards):
    totalDealerPoints = 0
    for card in dealerCards:
        values = int(card[2])
        totalDealerPoints += values
        # if totalDealerPoints == 21:
        #     print("DEALER POINTS: ", totalDealerPoints, "\nBLACKJACK !!!")
        #     exit()
        # elif totalDealerPoints > 21:
        #             for card in dealerCards:
        #                 if card[0] == "Ace":
        #                     card[2] == 1
        #                     dealerPoints(dealerCards)
    return totalDealerPoints

def dealerTurnHit(cards, dealerCards, dCard1, dCard2, playerCards, playerMoney, betAmount):
    print("DEALER's CARDS: ")
    print(dCard1[1], " of ", dCard1[0])
    print(dCard2[1], " of ", dCard2[0])
    print("DEALER POINTS: ", dealerPoints(dealerCards))

    while dealerPoints(dealerCards) < 17:
        print("\nDealer hits...\n")
        dCard3 = getDealerCards(cards, dealerCards)
        print(dCard3[1], " of ", dCard3[0])
        print("\nDEALER POINTS: ", dealerPoints(dealerCards))
    
    checkWinner(playerCards, dealerCards, playerMoney, betAmount)

def checkWinner(playerCards, dealerCards, playerMoney, betAmount):

    totalPlayerPoints = playerPoints(playerCards)
    totalDealerPoints = dealerPoints(dealerCards)

    if totalPlayerPoints > 21:
        for card in playerCards:
            values = card[2]
            if values == 11:
                values = 1
                totalPlayerPoints -= 10
            break
        print("BUST!! HA HA SUCKS TO BE YOU")
        exit()
    elif totalPlayerPoints == 21:
        print("\nBLACKJACK !!! You must have cheated, you're not THAT good...")
        playerWins(playerMoney, betAmount)
        exit()
    elif totalPlayerPoints < 21:
        if totalDealerPoints > 21:
                print(totalDealerPoints, " BUST!! DEALER LOSES, VICTORY!")
                print("MONEY: ", playerMoney)
                winnings = playerMoney * 1.5
                db.writePlayerMoney(playerMoney)
                exit()
        elif totalDealerPoints == 21:
            print("\nDEALER CARDS: ")
            print(dealerCards[0], dealerCards[1])
            print(totalDealerPoints, "\nBLACKJACK !!! DEALER WINS!")
            db.writePlayerMoney(playerMoney)
            exit()
        elif totalDealerPoints < 21:
            if totalPlayerPoints > totalDealerPoints:
                print("PLAYER WINS WITH ", totalPlayerPoints, " POINTS!")
                playerMoney = float(playerMoney) * 1.5
                db.writePlayerMoney(playerMoney)
                exit()
            elif totalPlayerPoints == totalDealerPoints:
                print("IT'S A DRAW!")
            else:
                print("YOU LOSE SUCKER !")
                print("MONEY: ", playerMoney)
                db.writePlayerMoney(playerMoney)
                exit()
    #Round payout to max 2 decimal places

def main():
    
    playerMoney = db.startingPlayerMoney()
    db.writePlayerMoney(playerMoney)

    print("BLACKJACK!")
    print("Blackjack payout os 3:2\n")
    
    cards = cardDeck()
    playerCards = []
    dealerCards = []

    betAmount = getPlayerBet(playerMoney)
    
    pCard1 = getPlayerCards(cards, playerCards)
    pCard2 = getPlayerCards(cards, playerCards)
    dCard1 = getDealerCards(cards, dealerCards)
    dCard2 = getDealerCards(cards, dealerCards)

    DealCards(pCard1, pCard2, dCard1, playerCards)
    totalPlayerPoints = playerPoints(playerCards, dealerCards, playerMoney)
    totalDealerPoints = dealerPoints(dealerCards)
    while totalPlayerPoints < 21 and totalDealerPoints <21:
        playerChoice = input("\nHit or Stand? >> ")
        if playerChoice.lower() == "hit":
            playerTurnHit(cards, playerCards)
            playerPoints(playerCards, dealerCards, playerMoney)
            #dealerPoints(dealerCards)
            #checkWinner(playerCards, dealerCards)
        elif playerChoice.lower() == "stand":
            #playerTurnStand(cards, dealerCards, dCard1, dCard2, playerCards, playerMoney, betAmount)
            dealerTurnHit(cards, playerCards, dealerCards, dCard1, dCard2, playerMoney, betAmount)
            checkWinner(playerCards, dealerCards, playerMoney, betAmount)
        else:
            print("Please enter a valid command.")

if __name__ == "__main__":
    main()
