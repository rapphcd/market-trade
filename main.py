from time import sleep
from classes import Game
from commands import handleBuyCommand
from utils import askUser, askUserAmount


def runRound(game):
    end = 0

    while end == 0:
        command = input("/").split(" ")

        if(command[0] == "buy"):
            command.pop(0)
            handleBuyCommand(command,game)

        elif command[0] == "sell" :
            return
            selectedStock = stocks[askUser("Sur quelle action voulez vous agir", ["g", "t", "r"])]

            if player.ressources[selectedStock] == 0:
                print("You don't have any of this ressource.")
                continue

            print("==================")
            print(f"{selectedStock.capitalize()}")
            print("==================")
            amount = askUserAmount("How many ?", 0, player.ressources[selectedStock])
            player.sellRessource(game.stockRessources[selectedStock], amount)
        else :
            print("Invalid command.")
            continue


def startGame():
    game = Game("Raph")

    round = 0
    while round <= 10:
        round += 1
        game.market.displayMarket()
        runRound(game)
        player.displayWallet()
        sleep(3)

if __name__ == "__main__":
    startGame()
