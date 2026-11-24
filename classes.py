from random import  randint

RESOURCES = ["sol", "btc", "gold", "eur", "eth"]

class Resource:
    def __init__(self, n, p):
        self.name = n
        self.price = p

    def displayName(self):
        return self.name.capitalize()

class Market:
    def __init__(self, r):
        self.prevPrices = [e.price for e in r]
        self.resources = r.copy()
        self.nextPrices = [e.price for e in r]

    def displayMarket(self):
        print("==================")
        print("Market")
        print("------------------")
        for i in range(len(self.resources)):
            resource = self.resources[i]
            old_price = self.prevPrices[i]

            print(f"{resource.displayName()}: {resource.price}$   {"+" if resource.price > old_price else ""}{resource.price - old_price}$")
        print("==================")

    def prepareNextMarket(self):
        nextPrices = []
        for res in self.resources:
            direction = randint(0,1)

            if direction == 1:
                nextPrices.append(res.price + randint(2, 10))
            else:
                nextPrices.append(res.price - max(0, randint(2, 10)))

        self.nextPrices = nextPrices

    def updateMarket(self):
        self.prevPrices = [e.price for e in self.resources]

        for i in range(len(self.resources)):
            self.resources[i].price = self.nextPrices[i]

class Player:
    def __init__(self, user_name):
        self.wallet = 100
        self.name = user_name

        resources = {}

        for resource in RESOURCES:
            resources[resource] = 0

        self.resources = resources

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


class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)

        resources = []
        stockResources = {}

        for resource in RESOURCES:
            res = Resource(resource, 30)
            resources.append(res)
            stockResources[resource] = res

        self.market = Market(resources)

        self.stockResources = stockResources

    def displayPlayerWallet(self):
        player = self.player
        total = player.wallet
        empty = True

        print("==================")
        print(f"Wallet: {player.wallet}$")
        print("------------------")

        for [k, v] in player.resources.items():
            total += v * self.stockResources[k].price
            if v > 0:
                empty = False
                print(f"{k.capitalize()}: {v}")

        if not empty:
            print("------------------")
        print(f"Total: : {total}$")
        print("==================")

    def end(self):
        self.player.displayWallet()
        money = self.player.wallet
        for [k,v] in self.player.resources.items():
            money += v * self.stockResources[k].price
        won = "won"
        if money < 450 :
            won = "lost"

        print("==================")
        print(f"You {won} with {money}$")
        print("==================")