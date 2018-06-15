from enum import Enum, unique


@unique
class Ordinal(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'O'

    @staticmethod
    def find_position(x, y, letter):
        return {
            Ordinal.NORTH.value: (x - 1, y),
            Ordinal.SOUTH.value: (x + 1, y),
            Ordinal.WEST.value: (x, y - 1),
            Ordinal.EAST.value: (x, y + 1)
        }.get(letter, (x, y))