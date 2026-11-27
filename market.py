from random import  randint

class Market:
    def __init__(self, r, game):
        self.prevPrices = [e.price for e in r]
        self.resources = r.copy()
        self.nextPrices = [e.price for e in r]
        self.game = game

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
            gap = randint(-10,10)
            new_price = res.price + gap

            if new_price < 1:
                new_price = 1

            nextPrices.append(new_price)

        self.nextPrices = nextPrices

    def updateMarket(self):
        self.prevPrices = [e.price for e in self.resources]

        for i in range(len(self.resources)):
            self.resources[i].price = self.nextPrices[i]
        self.game.updatePrices()