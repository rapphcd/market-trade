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

    def displayWallet(self):
        print("==================")
        print(f"Wallet: {self.wallet}")
        print("==================")
        print("Stocks:")
        for [k, v] in self.ressources.items():
            print(f"    {k.capitalize()}: {v}")
        print("==================")


def actOnStock(player, stock):
    print("==================")
    print(f"{stock.capitalize()}")
    print("==================")
    choice = input("You want to buy or sell (b | s): ")
    while choice not in ["b", "s"]:
        choice = input("You want to buy or sell (b | s): ")
    amount = int(input("How many: "))
    while math.isnan(amount):
        amount = int(input("How many: "))
    if (choice == "b"):
        player.buyAction(stock, amount)
    else:
        print("e")

def runRound(player):
    choice = input("Sur quelle action voulez vous agir (g | t | r): ")
    while choice not in ["g", "t", "r"]:
        choice = input("Sur quelle action voulez vous agir (g | t | r): ")
    actOnStock(player, stocks[choice])


def startGame():
    player = Player("Raph")
    player.displayWallet()
    runRound(player)
    player.displayWallet()


if __name__ == "__main__":
    startGame()
