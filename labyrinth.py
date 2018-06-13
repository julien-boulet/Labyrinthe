class Labyrinth:

    def __init__(self, robot, exit, walls, doors, grid):
        self.robot = robot
        self.exit = exit
        self.walls = walls
        self.doors = doors
        self.grid = grid

    def draw_it(self):
        for line in self.grid:
            for case in line:
                print(case, end='', flush=True)
            print('\n', end='', flush=True)

    def move_robot(self, letter):
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

        if (new_robot_x, new_robot_y) in self.walls:
            return False, False

        character_to_draw = ' '
        if (robot_x, robot_y) in self.doors:
            character_to_draw = '.'

        self.grid[robot_x][robot_y] = character_to_draw
        self.robot = new_robot
        self.grid[self.robot[0]][self.robot[1]] = 'X'

        if self.robot == self.exit:
            return True, True

        return True, False

    def read_content(content):

        lines = content.split("\n")

        walls = []
        doors = []
        grid = []

        for x, line in enumerate(lines):
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
