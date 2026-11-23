class Ressource:
    def __init__(self, n, p):
        self.name = n
        self.price = p
        self.oldPrice = p

    def displayName(self):
        return self.name.capitalize()

class Market:
    def __init__(self, r):
        self.ressources = r

    def displayMarket(self):
        print("==================")
        print("Market")
        print("------------------")
        for ressource in self.ressources:
            print(f"{ressource.displayName()}: {ressource.price}$")
        print("==================")

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

    def addRessource(self, stock, amount):
        self.ressources[stock] += amount

    def removeRessource(self, stock, amount):
        self.ressources[stock] -= amount

    def buyRessource(self, ressource, amount):
        self.addRessource(ressource.name, amount)
        self.removeMoney(ressource.price * amount)

    def sellRessource(self, ressource, amount):
        self.removeRessource(ressource.name, amount)
        self.addMoney(ressource.price * amount)

    def displayWallet(self):
        print("==================")
        print(f"Wallet: {self.wallet}")
        print("==================")
        print("Stocks:")
        for [k, v] in self.ressources.items():
            print(f"    {k.capitalize()}: {v}")
        print("==================")

class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)

        gold = Ressource("gold", 9)
        tokens = Ressource("tokens", 5)
        ram = Ressource("RAM", 14)

        self.market = Market([gold, tokens, ram])

        self.stockRessources = {
            "gold": gold,
            "tokens": tokens,
            "RAM": ram
        }