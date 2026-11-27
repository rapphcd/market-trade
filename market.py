from random import  randint

class Market:
    def __init__(self, r, game):
        self.prevPrices = [e.price for e in r]
        self.resources = r.copy()
        self.nextPrices = [e.price for e in r]
        self.game = game

    def updateMarket(self):
        self.prevPrices = [e.price for e in self.resources]

        for i in range(len(self.resources)):
            res = self.resources[i]
            gap = randint(-10, 10)
            new_price = res.price + gap

            if new_price < 1:
                new_price = 1

            self.resources[i].price = new_price

        self.game.updatePrices()