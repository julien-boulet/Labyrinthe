from enum import Enum, unique


@unique
class Element(Enum):
    WALL = 'O'
    DOOR = '.'
    EXIT = 'U'
    ROBOT = 'X'
    EMPTY = ' '
