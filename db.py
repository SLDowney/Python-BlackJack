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
