from enum import Enum, unique


@unique
class Ordinal(Enum):
    NORTH = ('N', -1, 0)
    SOUTH = ('S', +1, 0)
    WEST = ('O', 0, -1)
    EAST = ('E', 0, +1)

    def __init__(self, letter, x, y):
        self.letter = letter
        self.x = x
        self.y = y


    @staticmethod
    def find_by_letter(letter):
        return {
            Ordinal.NORTH.letter: Ordinal.NORTH,
            Ordinal.SOUTH.letter: Ordinal.SOUTH,
            Ordinal.WEST.letter: Ordinal.WEST,
            Ordinal.EAST.letter: Ordinal.EAST
        }.get(letter)

    def find_position(x, y, letter):
        return {
            Ordinal.NORTH.value: (x - 1, y),
            Ordinal.SOUTH.value: (x + 1, y),
            Ordinal.WEST.value: (x, y - 1),
            Ordinal.EAST.value: (x, y + 1)
        }.get(letter, (x, y))
