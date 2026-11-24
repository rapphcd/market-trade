import math

from classes import Market


def handleBuyCommand(args, game):
    player = game.player

    if len(args) < 2:
        print("Invalid args: /buy <resource> <amount>")
        return

    resource = args[0]


    if resource not in game.stockResources.keys():
        print("Invalid resource.")
        return

    if (args[1] == "max" or args[1] == "all"):
        amount = game.player.wallet // game.stockResources[resource].price
    else:
        amount = int(args[1])

    if math.isnan(amount):
        print("Invalid amount.")
        return
    if amount <= 0 :
        print("Too low.")
        return
    if amount > 10 - sum(player.resources.values()):
        print("Too big.")
        return

    print("==================")
    print(f"Bought {amount} {resource.capitalize()} for {amount*game.stockResources[resource].price}$")
    print("==================")

    player.buyResource(game.stockResources[resource], amount)

def handleSellCommand(args, game):
    player = game.player

    if len(args) < 2:
        print("Invalid args: /sell <resource> <amount>")
        return

    resource = args[0]

    if resource not in game.stockResources.keys():
        print("Invalid resource.")
        return

    if (args[1] == "all" or args[1] == "max"):
        amount = player.resources[resource]
    else:
        amount = int(args[1])

    if math.isnan(amount):
        print("Invalid resource.")
        return
    if amount <= 0:
        print("Too low.")
        return
    if amount > player.resources[resource]:
        print("Too big.")
        return

    print("==================")
    print(f"Sold {amount} {resource.capitalize()} for {amount * game.stockResources[resource].price}$")
    print("==================")

    player.sellResource(game.stockResources[resource], amount)

def handleMarketCommand(game):
    game.market.displayMarket()

def handleInvCommand(game):
    game.player.displayWallet()