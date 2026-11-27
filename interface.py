import customtkinter
import customtkinter as ctk

customtkinter.set_appearance_mode("system")

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
