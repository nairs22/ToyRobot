class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, position):
        return Position(self.x + position.x, self.y + position.y)
