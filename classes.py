class Resource:
    def __init__(self, n, p):
        self.name = n
        self.price = p
        self.oldPrice = p

    def displayName(self):
        return self.name.capitalize()

class Market:
    def __init__(self, r):
        self.resources = r

    def displayMarket(self):
        print("==================")
        print("Market")
        print("------------------")
        for resource in self.resources:
            print(f"{resource.displayName()}: {resource.price}$")
        print("==================")

class Player:
    def __init__(self, user_name):
        self.wallet = 100
        self.name = user_name
        self.resources = {
            "gold": 0,
            "tokens": 0,
            "RAM": 0
        }

    def addMoney(self, amount):
        self.wallet += amount

    def removeMoney(self, amount):
        self.wallet -= amount

    def addResource(self, stock, amount):
        self.resources[stock] += amount

    def removeResource(self, stock, amount):
        self.resources[stock] -= amount

    def buyResource(self, resource, amount):
        self.addResource(resource.name, amount)
        self.removeMoney(resource.price * amount)

    def sellResource(self, resource, amount):
        self.removeResource(resource.name, amount)
        self.addMoney(resource.price * amount)

    def displayWallet(self):
        print("==================")
        print(f"Wallet: {self.wallet}$")
        print("------------------")
        print("Stocks:")
        for [k, v] in self.resources.items():
            print(f"    {k.capitalize()}: {v}")
        print("==================")

class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)

        gold = Resource("gold", 9)
        tokens = Resource("tokens", 5)
        ram = Resource("RAM", 14)

        self.market = Market([gold, tokens, ram])

        self.stockResources = {
            "gold": gold,
            "tokens": tokens,
            "RAM": ram
        }