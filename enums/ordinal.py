from enum import Enum, unique


@unique
class Ordinal(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'O'

