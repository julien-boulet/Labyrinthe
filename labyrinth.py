from robot import Robot
from enums.element import Element
from actions.action import Drill, Build


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
                if case == Element.ROBOT.value:
                    self.robot = Robot(x, y)
                elif case == Element.DOOR.value:
                    self.doors.append((x, y))
                elif case == Element.WALL.value:
                    self.walls.append((x, y))
                elif case == Element.EXIT.value:
                    self.exits.append((x, y))

                grid_line.append(case)

            self.grid.append(grid_line)

    def draw_it(self):

        """ dessine le labyrinth """

        for line in self.grid:
            for case in line:
                print(case, end='', flush=True)
            print('\n', end='', flush=True)

    def move_robot_number(self, enum_ordinal, number):

        if not number:
            number = 1

        """temp_robot = deepcopy(self.robot)"""
        temp_robot = Robot(self.robot.x, self.robot.y)

        j = int(number)
        possible = True
        win = False
        while possible and not win and j > 0:
            possible, win = self.move_robot(enum_ordinal, temp_robot)
            j = j - 1

        if possible:
            """ si la position avant le move etait une porte, il faut redessiner une porte sinon un vide """
            character_to_draw = Element.EMPTY.value
            if (self.robot.x, self.robot.y) in self.doors:
                character_to_draw = Element.DOOR.value
            self.grid[self.robot.x][self.robot.y] = character_to_draw

            """ mise a jour de la nouvelle position du robot et ajout du robot a la grille"""
            self.robot = temp_robot
            self.grid[self.robot.x][self.robot.y] = Element.ROBOT.value

        return possible, win

    def move_robot(self, enum_ordinal, robot):

        """ bouge si possible le robot suivant le choix de l'utilisateur """

        robot.move(enum_ordinal)

        """ si futur position est un mur, pas possible et pas gagné"""
        if (robot.x, robot.y) in self.walls:
            return False, False

        """ si la nouvelle position du robot est la position de la sortie, on a gagné ! """
        if (robot.x, robot.y) in self.exits:
            return True, True

        """ position possible mais sans victoire, on continue... """
        return True, False

    def drill_wall(self, enum_ordinal):
        return Drill(self.walls).action(enum_ordinal, self)

    def build_wall(self, enum_ordinal):
        return Build(self.doors).action(enum_ordinal, self)
