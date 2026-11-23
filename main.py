from time import sleep
from classes import Game
from commands import handleBuyCommand, handleSellCommand, handleInvCommand

def runRound(game):
    end = 0

    while end == 0:
        command = input("/").split(" ")

        if command[0] == "buy":
            command.pop(0)
            handleBuyCommand(command,game)
        elif command[0] == "sell" :
            command.pop(0)
            handleSellCommand(command, game)
        elif command[0] == "inv" :
            handleInvCommand(game)
        elif command[0] == "next":
            end = 1
        else :
            print("Invalid command.")
            continue


def startGame():
    game = Game("Raph")

    game.market.prepareNextMarket()
    round = 0
    while round <= 10:
        round += 1
        game.market.updateMarket()
        game.market.displayMarket()
        runRound(game)
        game.market.prepareNextMarket()


    game.end

if __name__ == "__main__":
    startGame()
