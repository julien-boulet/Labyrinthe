from enums.ordinal import Ordinal


class Robot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, letter):
        if letter == Ordinal.NORTH.get_value():
            self.x = self.x - 1
        elif letter == Ordinal.SOUTH.get_value():
            self.x = self.x + 1
        elif letter == Ordinal.WEST.get_value():
            self.y = self.y - 1
        elif letter == Ordinal.EAST.get_value():
            self.y = self.y + 1
