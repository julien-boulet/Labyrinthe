from enums.ordinal import Ordinal


class Robot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, letter):
        self.x, self.y = Ordinal.find_position(self.x, self.y, letter)
