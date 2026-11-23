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
        game.player.displayWallet()
        sleep(3)

if __name__ == "__main__":
    startGame()
