class Resource:
    def __init__(self, n, p):
        self.name = n
        self.price = p

    def displayName(self):
        return self.name.capitalize()
