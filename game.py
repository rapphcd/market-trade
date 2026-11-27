from main import RESOURCES
from player import Player
from resource import Resource
from market import Market
from interface import Interface
from commands import handleBuyCommand, handleSellCommand, handleInvCommand, handleMarketCommand

class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)


        resources = []
        stockResources = {}

        for resource in RESOURCES:
            res = Resource(resource, 30)
            resources.append(res)
            stockResources[resource] = res

        self.market = Market(resources, self)

        self.stockResources = stockResources

        self.interface = Interface(self)

        self.market.prepareNextMarket()
        self.market.updateMarket()

        self.interface.mainloop()

    def updatePrices(self):
        for res in self.market.resources:
            self.interface.resourcesLabels[res.name].configure(text=f"{res.name.capitalize()}: {res.price}")

    def startGame(self):
        self.market.prepareNextMarket()
        day = 0
        while day < 15:
            day += 1
            self.market.updateMarket()
            self.market.displayMarket()
            print(f"Day {day}")
            print("/buy , /sell , /inv , /market , /next")
            self.runRound()
            self.market.prepareNextMarket()

        self.end()

    def runRound(self):
        end = 0

        while end == 0:
            command = input("/").split(" ")

            if command[0] == "buy":
                command.pop(0)
                handleBuyCommand(command, self)
            elif command[0] == "sell":
                command.pop(0)
                handleSellCommand(command, self)
            elif command[0] == "inv":
                handleInvCommand(self)
            elif command[0] == "market":
                handleMarketCommand(self)
            elif command[0] == "next":
                end = 1
            else:
                print("Invalid command.")
                continue

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
        self.displayPlayerWallet()
        money = self.player.wallet

        for [k,v] in self.player.resources.items():
            money += (int(v) * int(self.stockResources[k].price))

        won = "won"
        if money < 450 :
            won = "lost"

        print("==================")
        print(f"You {won} with {money}$")
        print("==================")