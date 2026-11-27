from random import  randint

import customtkinter
import customtkinter as ctk

customtkinter.set_appearance_mode("system")

RESOURCES = ["sol", "btc", "gold", "eur", "eth"]

class Resource:
    def __init__(self, n, p):
        self.name = n
        self.price = p

    def displayName(self):
        return self.name.capitalize()

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

class Interface(customtkinter.CTk):
    def __init__(self, game):
        super().__init__()

        self.game = game

        self.title("Black Market")
        self.geometry("1200x800")
        self.grid_columnconfigure((0, 1), weight=1)

        self.marketcard = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="#242424",
            border_width=1,
            border_color="#383838"
        )

        self.marketcard.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        title = ctk.CTkLabel(
            self.marketcard,
            text="Market",
            text_color="#ffffff"
        )

        title.pack(padx=20, pady=10)

        resourcesLabels = {}

        for res in self.game.market.resources:
            value = ctk.CTkLabel(
                self.marketcard,
                text=f"{res.name.capitalize()}: {res.price}",
                text_color="#ffffff",
                font=("Arial", 32),
            )
            resourcesLabels[res.name] = value
            value.pack(pady=10, padx=10)

        self.resourcesLabels = resourcesLabels

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