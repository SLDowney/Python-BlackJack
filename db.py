def startingPlayerMoney():
    try:
        playerMoney = 100
        with open("money.txt", "w") as file:
            file.write(str(playerMoney))
        return playerMoney
    except FileNotFoundError:
        print("Error in starting Player Money function!")

def writePlayerMoney(playerMoney):
    try:
        with open("money.txt", "w") as file:
            file.write(str(playerMoney))
        return playerMoney
    except FileNotFoundError:
        print("Error finding file, creating new file.")
        playerMoney = [100]
        with open("money.txt", "w") as file:
            file.write(str(playerMoney))
        return playerMoney

def readPlayerMoney():
    with open("money.txt", "r") as file:
        playerMoney = file.read()
        #print(playerMoney)
        return playerMoney

#if __name__ == "__main__":
 #   main()