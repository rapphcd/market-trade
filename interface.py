import customtkinter
import customtkinter as ctk

customtkinter.set_appearance_mode("system")

class Interface(customtkinter.CTk):
    def __init__(self, game):
        super().__init__()

        self.game = game

        self.title("Black Market")
        self.geometry("1400x600")
        self.grid_columnconfigure((0, 1), weight=1)

        self.dayLabel = ctk.CTkLabel(
            self,
            text="Day 0",
            text_color="#000000",
            font=("Arial", 32, "bold")
        )
        self.marketcard = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="#ffffff",
            border_width=1,
            border_color="#d1d1d1"
        )
        self.invcard = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="#ffffff",
            border_width=1,
            border_color="#d1d1d1"
        )

        self.dayLabel.grid(row=0, column=0, padx=20, pady=20, columnspan=2)
        self.marketcard.grid(row=1, column=0,padx=10, sticky="nsew")
        self.invcard.grid(row=1, column=1, padx=10,  sticky="nsew")

        market_title = ctk.CTkLabel(
            self.marketcard,
            text="Market",
            text_color="#111111",
            font=("Arial", 24)
        )

        market_title.grid(row=0, column=1, padx=50, pady=20)

        inv_title = ctk.CTkLabel(
            self.invcard,
            text="Inventory",
            text_color="#111111",
            font=("Arial", 24)
        )

        inv_title.grid(row=0, column=1, padx=50, pady=20)

        self.totalLabel = ctk.CTkLabel(
            self.invcard,
            text=f"Total: {self.game.player.getTotal()}$",
            text_color="#111111",
            font=("Arial", 24)
        )

        self.walletLabel = ctk.CTkLabel(
            self.invcard,
            text=f"Wallet: {self.game.player.wallet}$",
            text_color="#111111",
            font=("Arial", 24)
        )

        next_button = ctk.CTkButton(
            self,
            text="Next",
            text_color="#ffffff",
            font=("Arial", 32),
            command=self.game.nextDay
        )

        next_button.grid(row=0, column=1, pady=10, padx=10, sticky="e")

        self.totalLabel.grid(row=2, column=2, padx=50, pady=20, sticky="e")
        self.walletLabel.grid(row=4, column=2, padx=50, pady=20, sticky="e")

        resourcesLabels = {}

        for i in range(len(self.game.market.resources)):
            res = self.game.market.resources[i]
            old_price = self.game.market.prevPrices[i]

            infos = ctk.CTkLabel(
                self.marketcard,
                text=f"{res.name.capitalize()}: {res.price}$",
                text_color="#111111",
                font=("Arial", 32)
            )

            prog = ctk.CTkLabel(
                self.marketcard,
                text=f"{"+" if res.price > old_price else ""}{res.price - old_price}$",
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

        self.resourcesLabels = resourcesLabels


    def initButtons(self):

        for i in range(len(self.game.market.resources)):
            res = self.game.market.resources[i]

            def buy_command(stock=res):
                self.game.player.buyResource(stock, 1)

            def sell_command(stock=res):
                self.game.player.sellResource(stock, 1)

            buy_button = ctk.CTkButton(
                self.marketcard,
                text="+",
                text_color="#ffffff",
                font=("Arial", 32),
                command=buy_command
            )

            sell_button = ctk.CTkButton(
                self.invcard,
                text="-",
                text_color="#ffffff",
                font=("Arial", 32),
                command=sell_command
            )

            buy_button.grid(row=i + 1, column=3, pady=10, padx=10, sticky="e")

            sell_button.grid(row=i + 1, column=1, pady=10, padx=10, sticky="w")

