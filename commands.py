import math

from classes import Player
from utils import askUser, askUserAmount, stocks

def handleBuyCommand(args, game):
    player = game.player

    if len(args) < 2:
        print("Invalid args: /buy <ressource> <amount>")
        return

    ressource = args[0]
    amount = int(args[1])

    if ressource not in game.stockRessources.keys():
        print("Invalid resource.")
        return
    if math.isnan(amount):
        print("Invalid resource.")
        return
    if amount <= 0 :
        print("Too low.")
        return
    if amount > 10 - sum(player.ressources.values()):
        print("Too big.")
        return

    print("==================")
    print(f"Bought {amount} {ressource.capitalize()} for {amount*game.stockRessources[ressource].price}$")
    print("==================")

    player.buyRessource(game.stockRessources[ressource], amount)

def handleSellCommand(args, game):
    player = game.player

    if len(args) < 2:
        print("Invalid args: /sell <ressource> <amount>")
        return

    ressource = args[0]
    amount = int(args[1])

    if ressource not in game.stockRessources.keys():
        print("Invalid resource.")
        return
    if math.isnan(amount):
        print("Invalid resource.")
        return
    if amount <= 0:
        print("Too low.")
        return
    if amount > player.ressources[ressource]:
        print("Too big.")
        return

    print("==================")
    print(f"Sold {amount} {ressource.capitalize()} for {amount * game.stockRessources[ressource].price}$")
    print("==================")

    player.sellRessource(game.stockRessources[ressource], amount)