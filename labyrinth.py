class Labyrinth:

    def __init__(self, robot, exit, walls, doors, grid):
        self.robot = robot
        self.exit = exit
        self.walls = walls
        self.doors = doors
        self.grid = grid

    def draw_it(self):

        """ dessine le labyrinth """

        for line in self.grid:
            for case in line:
                print(case, end='', flush=True)
            print('\n', end='', flush=True)

    def move_robot(self, letter):

        """ bouge si possible le robot suivant le choix de l'utilisateur """

        robot_x = self.robot[0]
        robot_y = self.robot[1]

        if letter == 'N':
            new_robot = (robot_x - 1, robot_y)
        elif letter == 'S':
            new_robot = (robot_x + 1, robot_y)
        elif letter == 'O':
            new_robot = (robot_x, robot_y - 1)
        elif letter == 'E':
            new_robot = (robot_x, robot_y + 1)

        new_robot_x = new_robot[0]
        new_robot_y = new_robot[1]

        """ si futur position est un mur """
        if (new_robot_x, new_robot_y) in self.walls:
            return False, False

        """ si la position avant le move etait une porte, il faut redessiner une porte sinon un vide """
        character_to_draw = ' '
        if (robot_x, robot_y) in self.doors:
            character_to_draw = '.'
        self.grid[robot_x][robot_y] = character_to_draw

        """ mise a jour de la nouvelle position du robot et ajout du robot a la grille"""
        self.robot = new_robot
        self.grid[self.robot[0]][self.robot[1]] = 'X'

        """ si la nouvelle position du robot est la position de la sortie, on a gagné ! """
        if self.robot == self.exit:
            return True, True

        """ position possible mais sans vistoire, on continue... """
        return True, False

    def read_content(content):

        """ construit un labyrinth à partir du contenu du fichier text """

        walls = []
        doors = []
        grid = []

        for x, line in enumerate(content.split("\n")):
            grid_line = []
            for y, case in enumerate(line):
                if case == 'X':
                    robot = (x, y)
                elif case == '.':
                    doors.append((x, y))
                elif case == 'O':
                    walls.append((x, y))
                elif case == 'U':
                    exit = (x, y)
                grid_line.append(case)
            grid.append(grid_line)

        return Labyrinth(robot, exit, walls, doors, grid)
