import math
from time import sleep
from classes import Ressource, Market, Player


stocks = {
    "g": "gold",
    "t": "tokens",
    "r": "RAM"
}

stockPrice = {
    "gold": 7,
    "tokens": 4,
    "RAM": 12
}

def askUser(message, choices):
    choice = input(f"{message} ({' | '.join(choices)}): ")
    while choice not in choices:
        choice = input(f"{message} ({' | '.join(choices)}): ")
    return choice

def askUserAmount(message, min, max):
    choice = int(input(f"{message} (min: {min} | max: {max}): "))
    while math.isnan(choice) or choice < min or choice > max :
        choice = int(input(f"{message} (min: {min} | max: {max}): "))
    return choice

def runRound(player):
    end = 0

    while end == 0:
        command = input("/").split(" ")
        return ;
        if(command[0] == "buy"):
            selectedStock = stocks[askUser("Sur quelle action voulez vous agir", ["g", "t", "r"])]

            print("==================")
            print(f"{selectedStock.capitalize()}")
            print("==================")
            amount = askUserAmount("How many ?", 0, 10 - sum(player.ressources.values()))
            player.buyRessource(selectedStock, amount)

        elif command[0] == "sell" :
            selectedStock = stocks[askUser("Sur quelle action voulez vous agir", ["g", "t", "r"])]

            if player.ressources[selectedStock] == 0:
                print("You don't have any of this ressource.")
                continue

            print("==================")
            print(f"{selectedStock.capitalize()}")
            print("==================")
            amount = askUserAmount("How many ?", 0, player.ressources[selectedStock])
            player.sellRessource(selectedStock, amount)
        else :
            print("Invalid command.")
            continue


def startGame():
    player = Player("Raph")

    gold = Ressource("gold", 9)
    tokens = Ressource("tokens", 5)
    ram = Ressource("RAM", 14)

    market = Market([gold, tokens, ram])

    round = 0
    while round <= 10:
        round += 1
        market.displayMarket()
        runRound(player)
        player.displayWallet()
        sleep(3)

if __name__ == "__main__":
    startGame()
