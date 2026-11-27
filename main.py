from game import Game
from commands import handleBuyCommand, handleSellCommand, handleInvCommand, handleMarketCommand

RESOURCES = ["sol", "btc", "gold", "eur", "eth"]

def runRound(game):
    end = 0

    while end == 0:
        command = input("/").split(" ")

        if command[0] == "buy":
            command.pop(0)
            handleBuyCommand(command, game)
        elif command[0] == "sell":
            command.pop(0)
            handleSellCommand(command, game)
        elif command[0] == "inv":
            handleInvCommand(game)
        elif command[0] == "market":
            handleMarketCommand(game)
        elif command[0] == "next":
            end = 1
        else:
            print("Invalid command.")
            continue


def startGame():
    game = Game("Raph")

    game.market.prepareNextMarket()
    day = 0
    while day < 15:
        day += 1
        game.market.updateMarket()
        game.market.displayMarket()
        print(f"Day {day}")
        print("/buy , /sell , /inv , /market , /next")
        runRound(game)
        game.market.prepareNextMarket()

    game.end()

if __name__ == "__main__":
    startGame()
