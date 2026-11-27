import customtkinter
import customtkinter as ctk
from matplotlib.ticker import MultipleLocator

from config import RESOURCES_COLORS
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

customtkinter.set_appearance_mode("light")

class Interface(customtkinter.CTk):
    def __init__(self, game):
        super().__init__()

        self.game = game

        self.title("Black Market")
        self.geometry("1400x900")
        self.grid_columnconfigure((0, 1), weight=1)

        self.dayLabel = ctk.CTkLabel(
            self,
            text="Day 0",
            text_color="#000000",
            font=("Arial", 32, "bold")
        )

        self.next_button = ctk.CTkButton(
            self,
            text="Next day",
            text_color="#ffffff",
            font=("Arial", 32),
            command=self.game.nextDay
        )

        self.next_button.grid(row=0, column=1, pady=10, padx=10, sticky="e")
        self.dayLabel.grid(row=0, column=0, padx=20, pady=0, columnspan=2)

        self.marketcard = self.initMarket()
        self.invcard, self.totalLabel, self.walletLabel = self.initInv()
        self.resourcesLabels = self.initMarketRows()
        self.graph, self.resourcesLines, self.canvas = self.initGraph()

    def initMarket(self):
        marketcard = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="#ffffff",
            border_width=1,
            border_color="#d1d1d1"
        )
        market_title = ctk.CTkLabel(
            marketcard,
            text="Market",
            text_color="#111111",
            font=("Arial", 28, "bold")
        )

        marketcard.grid(row=1, column=0, padx=10, sticky="nsew")
        market_title.grid(row=0, column=0, padx=50, pady=20)
        return marketcard

    def initInv(self):
        invcard = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="#ffffff",
            border_width=1,
            border_color="#d1d1d1"
        )

        inv_title = ctk.CTkLabel(
            invcard,
            text="Inventory",
            text_color="#111111",
            font=("Arial", 28, "bold")
        )

        totalLabel = ctk.CTkLabel(
            invcard,
            text=f"Total: {self.game.player.getTotal()}$",
            text_color="#111111",
            font=("Arial", 24)
        )

        walletLabel = ctk.CTkLabel(
            invcard,
            text=f"Wallet: {self.game.player.wallet}$",
            text_color="#111111",
            font=("Arial", 24)
        )

        invcard.grid(row=1, column=1, padx=10, sticky="nsew")
        inv_title.grid(row=0, column=0, padx=50, pady=20)
        totalLabel.grid(row=2, column=3, padx=50, pady=20, sticky="w")
        walletLabel.grid(row=4, column=3, padx=50, pady=20, sticky="w")

        return invcard, totalLabel, walletLabel

    def initMarketRows(self):
        resourcesLabels = {}

        for i in range(len(self.game.market.resources)):
            res = self.game.market.resources[i]

            infos = ctk.CTkLabel(
                self.marketcard,
                text=f"{res.name.capitalize()}: {res.price}$",
                text_color="#111111",
                font=("Arial", 32)
            )

            prog = ctk.CTkLabel(
                self.marketcard,
                text="--",
                text_color="#111111",
                font=("Arial", 32)
            )

            inv = ctk.CTkLabel(
                self.invcard,
                text=f"{res.name.capitalize()}: {self.game.player.resources[res.name]}",
                text_color="#111111",
                font=("Arial", 32)
            )

            infos.grid(row=i + 1, column=0, pady=10, padx=10, sticky="w")
            prog.grid(row=i + 1, column=2, pady=10, padx=10, sticky="w")
            inv.grid(row=i + 1, column=0, pady=10, padx=10, sticky="w")

            resourcesLabels[res.name] = {"infos": infos, "prog": prog, "inv": inv}

        return resourcesLabels

    def initGraph(self):
        figure = Figure(figsize=(16, 4), dpi=100)
        graph = ax = figure.add_subplot(111)
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.set_xlim(1, 15)
        ax.set_xticks(range(0, 16))

        resourcesLines = {}

        for res in self.game.market.resources:
            resourcesLines[res.name], = ax.plot(self.game.days, self.game.prices[res.name], color=RESOURCES_COLORS[res.name], marker="o")

        ax.set_title("Market evolution")
        ax.set_xlabel("Day")
        ax.set_ylabel("Price")
        ax.grid(True, alpha=0.3)

        canvas = FigureCanvasTkAgg(figure, master=self)
        canvas.draw()

        canvas.get_tk_widget().grid(row=2, column=0, padx=20, pady=10, columnspan=2)
        return graph, resourcesLines, canvas

    def initButtons(self):

        for i in range(len(self.game.market.resources)):
            res = self.game.market.resources[i]

            def buy_command(stock=res):
                self.game.player.buyResource(stock, 1)

            def buy_max_command(stock=res):
                self.game.player.buyResource(stock, self.game.player.wallet // stock.price)

            def sell_command(stock=res):
                self.game.player.sellResource(stock, 1)

            def sell_max_command(stock=res):
                self.game.player.sellResource(stock, self.game.player.resources[stock.name])

            buy_button = ctk.CTkButton(
                self.marketcard,
                text="Buy 1",
                text_color="#ffffff",
                font=("Arial", 32),
                command=buy_command
            )

            buy_max = ctk.CTkButton(
                self.marketcard,
                text="Buy all",
                text_color="#ffffff",
                font=("Arial", 32),
                command=buy_max_command
            )

            sell_button = ctk.CTkButton(
                self.invcard,
                text="Sell 1",
                text_color="#ffffff",
                font=("Arial", 32),
                command=sell_command
            )

            sell_max = ctk.CTkButton(
                self.invcard,
                text="Sell all",
                text_color="#ffffff",
                font=("Arial", 32),
                command=sell_max_command
            )

            buy_button.grid(row=i + 1, column=3, pady=10, padx=10, sticky="e")
            buy_max.grid(row=i + 1, column=4, pady=10, padx=10, sticky="e")

            sell_button.grid(row=i + 1, column=1, pady=10, padx=10, sticky="e")
            sell_max.grid(row=i + 1, column=2, pady=10, padx=10, sticky="e")

    def updateGraph(self):
        for res in self.game.market.resources:
            self.resourcesLines[res.name], = self.graph.plot(self.game.days, self.game.prices[res.name], color=RESOURCES_COLORS[res.name], marker="o")

        self.graph.relim()
        self.graph.autoscale_view()

        self.canvas.draw_idle()

    def updateInvForStock(self, stock):
        self.resourcesLabels[stock]["inv"].configure(text=f"{stock.capitalize()}: {self.game.player.resources[stock]}")
        self.updateTotalLabel()

    def updateTotalLabel(self):
        self.totalLabel.configure(text=f"Total: {self.game.player.getTotal()}$")

    def updateWalletLabel(self):
        self.walletLabel.configure(text=f"Wallet: {self.game.player.wallet}$")