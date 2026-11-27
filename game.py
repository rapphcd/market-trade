from main import RESOURCES
from player import Player
from resource import Resource
from market import Market
from interface import Interface

class Game:
    def __init__(self, player_name):
        self.player = Player(player_name, self)
        self.interface = None

        self.day = 0

        resources = []
        stockResources = {}
        prices = {}

        for resource in RESOURCES:
            res = Resource(resource, 30)
            resources.append(res)
            stockResources[resource] = res
            prices[resource] = [30]

        self.days = [0]
        self.prices = prices

        self.market = Market(resources, self)

        self.stockResources = stockResources

        self.interface = Interface(self)

    def updatePrices(self):
        self.days.append(self.day)
        for i in range(len(self.market.resources)):
            res = self.market.resources[i]
            old_price = self.market.prevPrices[i]

            self.prices[res.name].append(res.price)

            self.interface.resourcesLabels[res.name]["infos"].configure(text=f"{res.name.capitalize()}: {res.price}$")

            if self.day > 1:
                self.interface.resourcesLabels[res.name]["prog"].configure(text=f"{"+" if res.price > old_price else ""}{res.price - old_price}$", text_color=f"{"#00FF00" if res.price >= old_price else "#FF0000"}")

    def startGame(self):

        self.interface.initButtons()
        self.nextDay()
        self.interface.mainloop()

    def nextDay(self):

        self.day +=1
        self.market.prepareNextMarket()
        self.market.updateMarket()
        self.interface.dayLabel.configure(text=f"Day {self.day}")
        self.player.updateTotalLabel()
        self.interface.updateGraph()

        if self.day == 16:
            self.end()
            return

    def exit(self):
        self.interface.destroy()

    def end(self):
        money = self.player.getTotal()

        won = "Won"
        if money < 450 :
            won = "Lost"

        self.interface.invcard.destroy()
        self.interface.marketcard.destroy()

        self.interface.dayLabel.configure(text=f"{won} with {money}$")
        self.interface.next_button.configure(text="Exit", command=self.exit)