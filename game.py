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

        for resource in RESOURCES:
            res = Resource(resource, 30)
            resources.append(res)
            stockResources[resource] = res

        self.market = Market(resources, self)

        self.stockResources = stockResources

        self.interface = Interface(self)

    def updatePrices(self):
        for i in range(len(self.market.resources)):
            res = self.market.resources[i]
            old_price = self.market.prevPrices[i]

            self.interface.resourcesLabels[res.name]["infos"].configure(text=f"{res.name.capitalize()}: {res.price}")
            self.interface.resourcesLabels[res.name]["prog"].configure(text=f"{"+" if res.price > old_price else ""}{res.price - old_price}$")

    def startGame(self):

        self.interface.initButtons()
        self.nextDay()
        self.interface.mainloop()

    def nextDay(self):
        if self.day == 15:
            self.end()
            return

        self.day +=1
        self.market.prepareNextMarket()
        self.market.updateMarket()
        self.interface.dayLabel.configure(text=f"Day {self.day}")
        self.player.updateTotalLabel()


    def end(self):
        money = self.player.wallet


        for [k,v] in self.player.resources.items():
            money += (int(v) * int(self.stockResources[k].price))

        won = "won"
        if money < 450 :
            won = "lost"

        print("==================")
        print(f"You {won} with {money}$")
        print("==================")