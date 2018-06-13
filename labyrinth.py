from robot import *
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
                if case == 'X':
                    self.robot = Robot(x, y)
                elif case == '.':
                    self.doors.append((x, y))
                elif case == 'O':
                    self.walls.append((x, y))
                elif case == 'U':
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
            possible, win, temp_robot = self.move_robot(letter, temp_robot)
            j = j - 1

        if possible:
            """ si la position avant le move etait une porte, il faut redessiner une porte sinon un vide """
            character_to_draw = ' '
            if (self.robot.x, self.robot.y) in self.doors:
                character_to_draw = '.'
            self.grid[self.robot.x][self.robot.y] = character_to_draw

            """ mise a jour de la nouvelle position du robot et ajout du robot a la grille"""
            self.robot = temp_robot
            self.grid[self.robot.x][self.robot.y] = 'X'

        return possible, win

    def move_robot(self, letter, robot):

        """ bouge si possible le robot suivant le choix de l'utilisateur """

        robot.move(letter)

        """ si futur position est un mur """
        if (robot.x, robot.y) in self.walls:
            return False, False, robot

        """ si la nouvelle position du robot est la position de la sortie, on a gagné ! """
        if (robot.x, robot.y) in self.exits:
            return True, True, robot

        """ position possible mais sans vistoire, on continue... """
        return True, False, robot
