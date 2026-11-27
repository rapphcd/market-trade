from main import RESOURCES

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