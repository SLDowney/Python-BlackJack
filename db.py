def startingPlayerMoney():
    try:
        playerMoney = [100]
        with open("money.txt", "w") as file:
            file.write(str(playerMoney))
        return playerMoney
    except FileNotFoundError:
        print("Error in starting Player Money function!")

def writePlayerMoney(playerMoney):
    try:
        with open("money.txt", "w") as file:
            file.write(str(playerMoney) + "\n")
        return playerMoney
    except FileNotFoundError:
        print("Error writing file.")
