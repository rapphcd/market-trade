class Player:
    def __init__(self, user_name):
        self.wallet = 100
        self.name = user_name
        self.ressources = {
            "gold": 0,
            "tokens": 0,
            "RAM": 0
        }

    def addMoney(self, amout):
        self.wallet += amout

    def removeMoney(self, amout):
        self.wallet -= amout

    def displayWallet(self):
        print("==================")
        print(f"Wallet: {self.wallet}")
        print("==================")

def startGame():
    player = Player("Raph")
    player.displayWallet()


if __name__ == "__main__":
    startGame()