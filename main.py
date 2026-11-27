from game import *

RESOURCES = ["sol", "btc", "gold", "eur", "eth"]
RESOURCES_COLORS = {
    "sol": "red",
    "btc": "royalblue",
    "gold": "orange",
    "eur": "green",
    "eth": "purple"
}

if __name__ == "__main__":
    game = Game("Raph")
    game.startGame()
