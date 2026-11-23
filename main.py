import math

stocks = {
    "g": "gold",
    "t": "tokens",
    "r": "RAM"
}

stockPrice = {
    "gold": 7,
    "tokens": 4,
    "RAM": 12
}


class Player:
    def __init__(self, user_name):
        self.wallet = 100
        self.name = user_name
        self.ressources = {
            "gold": 0,
            "tokens": 0,
            "RAM": 0
        }

    def addMoney(self, amout):
        self.wallet += amout

    def removeMoney(self, amout):
        self.wallet -= amout

    def buyAction(self, stock, amount):
        self.ressources[stock] += amount
        self.wallet -= amount * stockPrice[stock]

    def sellAction(self, stock, amount):
        self.ressources[stock] -= amount
        self.wallet += amount * stockPrice[stock]

    def displayWallet(self):
        print("==================")
        print(f"Wallet: {self.wallet}")
        print("==================")
        print("Stocks:")
        for [k, v] in self.ressources.items():
            print(f"    {k.capitalize()}: {v}")
        print("==================")

def askUser(message, choices):
    choice = input(f"{message} ({' | '.join(choices)}): ")
    while choice not in choices:
        choice = input(f"{message} ({' | '.join(choices)}): ")
    return choice

def askUserAmount(message, min, max):
    choice = int(input(f"{message} (min: {min} | max: {max}): "))
    while math.isnan(choice) or choice < min or choice > max :
        choice = int(input(f"{message} (min: {min} | max: {max}): "))
    return choice

def runRound(player):
    action = askUser("Do you want to buy or sell ?", ["b", "s"])
    selectedStock = stocks[askUser("Sur quelle action voulez vous agir", ["g", "t", "r"])]

    while player.ressources[selectedStock] == 0 and action == "s":
        print("You don't have any of this ressource.")
        action = askUser("Do you want to buy or sell ?", ["b", "s"])
        selectedStock = stocks[askUser("Sur quelle action voulez vous agir", ["g", "t", "r"])]


    print("==================")
    print(f"{selectedStock.capitalize()}")
    print("==================")

    if (action == "b"):
        amount = askUserAmount("How many ?", 0, 10 - sum(player.ressources.values()))
        player.buyAction(selectedStock, amount)
    else:
        amount = askUserAmount("How many ?", 0, player.ressources[selectedStock])
        player.sellAction(selectedStock, amount)


def startGame():
    player = Player("Raph")
    player.displayWallet()

    round = 0
    while round <= 10:
        round += 1
        runRound(player)
        player.displayWallet()



if __name__ == "__main__":
    startGame()
