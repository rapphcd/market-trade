import math

stocks = {
    "g": "gold",
    "t": "tokens",
    "r": "RAM"
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
