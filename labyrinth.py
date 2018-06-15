from robot import *
from enums.element import Element
from enums.ordinal import Ordinal
from copy import deepcopy


class Labyrinth:

    def __init__(self, content):
        """ construit un labyrinth à partir du contenu du fichier text """
        self.walls = []
        self.doors = []
        self.grid = []
        self.exits = []
        self.robot = None

        for x, line in enumerate(content.split("\n")):
            grid_line = []
            for y, case in enumerate(line):
                if case == Element.ROBOT.get_value():
                    self.robot = Robot(x, y)
                elif case == Element.DOOR.get_value():
                    self.doors.append((x, y))
                elif case == Element.WALL.get_value():
                    self.walls.append((x, y))
                elif case == Element.EXIT.get_value():
                    self.exits.append((x, y))

                grid_line.append(case)

            self.grid.append(grid_line)

    def draw_it(self):

        """ dessine le labyrinth """

        for line in self.grid:
            for case in line:
                print(case, end='', flush=True)
            print('\n', end='', flush=True)

    def move_robot_number(self, letter, number):

        if not number:
            number = 1

        """temp_robot = deepcopy(self.robot)"""
        temp_robot = Robot(self.robot.x, self.robot.y)

        j = int(number)
        possible = True
        win = False
        while possible and not win and j > 0:
            possible, win = self.move_robot(letter, temp_robot)
            j = j - 1

        if possible:
            """ si la position avant le move etait une porte, il faut redessiner une porte sinon un vide """
            character_to_draw = Element.EMPTY.get_value()
            if (self.robot.x, self.robot.y) in self.doors:
                character_to_draw = Element.DOOR.get_value()
            self.grid[self.robot.x][self.robot.y] = character_to_draw

            """ mise a jour de la nouvelle position du robot et ajout du robot a la grille"""
            self.robot = temp_robot
            self.grid[self.robot.x][self.robot.y] = Element.ROBOT.get_value()

        return possible, win

    def move_robot(self, letter, robot):

        """ bouge si possible le robot suivant le choix de l'utilisateur """

        robot.move(letter)

        """ si futur position est un mur """
        if (robot.x, robot.y) in self.walls:
            return False, False

        """ si la nouvelle position du robot est la position de la sortie, on a gagné ! """
        if (robot.x, robot.y) in self.exits:
            return True, True

        """ position possible mais sans vistoire, on continue... """
        return True, False

    def drill_wall(self, letter_direction):
        (x, y) = Labyrinth.find_position(self.robot.x, self.robot.y, letter_direction)

        if (x, y) in self.walls:
            self.walls.remove((x, y))
            self.doors.append((x, y))
            self.grid[x][y] = Element.DOOR.get_value()
            return True
        else:
            return False

    def build_wall(self, letter_direction):
        (x, y) = Labyrinth.find_position(self.robot.x, self.robot.y, letter_direction)

        if (x, y) in self.doors:
            self.walls.append((x, y))
            self.doors.remove((x, y))
            self.grid[x][y] = Element.WALL.get_value()
            return True
        else:
            return False

    @staticmethod
    def find_position(x, y, letter):
        return {
            Ordinal.NORTH.get_value(): (x - 1, y),
            Ordinal.SOUTH.get_value(): (x + 1, y),
            Ordinal.WEST.get_value(): (x, y - 1),
            Ordinal.EAST.get_value(): (x, y + 1)
        }.get(letter, (x, y))
