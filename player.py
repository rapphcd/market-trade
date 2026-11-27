from config import RESOURCES

class Player:
    def __init__(self, user_name, game):
        self.wallet = 100
        self.name = user_name

        resources = {}

        for resource in RESOURCES:
            resources[resource] = 0

        self.resources = resources

        self.game = game

    def addMoney(self, amount):
        self.wallet += amount
        self.game.interface.updateWalletLabel()

    def removeMoney(self, amount):
        self.wallet -= amount
        self.game.interface.updateWalletLabel()

    def addResource(self, stock, amount):
        self.resources[stock] += amount
        self.game.interface.updateInvForStock(stock)

    def removeResource(self, stock, amount):
        self.resources[stock] -= amount
        self.game.interface.updateInvForStock(stock)

    def buyResource(self, resource, amount):
        if self.wallet < resource.price * amount:
            return

        self.removeMoney(resource.price * amount)
        self.addResource(resource.name, amount)

    def sellResource(self, resource, amount):
        if self.resources[resource.name] == 0 or self.resources[resource.name] < amount:
            return

        self.addMoney(resource.price * amount)
        self.removeResource(resource.name, amount)

    def getTotal(self):
        total = self.wallet
        for [k, v] in self.resources.items():
            total += v * self.game.stockResources[k].price

        return total