from utils import askUser, askUserAmount, stocks

def handleBuyCommand(args, game):
    player = game.player

    selectedStock = stocks[askUser("Sur quelle action voulez vous agir", ["g", "t", "r"])]

    print("==================")
    print(f"{selectedStock.capitalize()}")
    print("==================")
    amount = askUserAmount("How many ?", 0, 10 - sum(player.ressources.values()))
    player.buyRessource(game.stockRessources[selectedStock], amount)