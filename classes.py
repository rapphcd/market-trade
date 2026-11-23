from random import  randint

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
        self.nextResources = r

    def displayMarket(self):
        print("==================")
        print("Market")
        print("------------------")
        for resource in self.resources:
            print(f"{resource.displayName()}: {resource.price}$")
        print("==================")

    def prepareNextMarket(self):
        nextResources = []
        for res in self.resources:
            direction = randint(0,1)
            amount = randint(2, 10)

            if direction == 1:
                res.price += amount
            else:
                if res.price <= amount:
                    res.price = 1
                else:
                    res.price -= amount

            nextResources.append(res)
        self.nextResources = nextResources

    def updateMarket(self):
        self.resources = self.nextResources

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

        gold = Resource("gold", 30)
        tokens = Resource("tokens", 30)
        ram = Resource("RAM", 30)

        self.market = Market([gold, tokens, ram])

        self.stockResources = {
            "gold": gold,
            "tokens": tokens,
            "RAM": ram
        }

    def end(self):
        self.player.displayWallet()
        money = self.player.wallet
        for res in self.player.resources.values():
            money += res
        won = "won"
        if money < 500 :
            won = "lost"

        print("==================")
        print(f"You {won} with {money}$")
        print("==================")