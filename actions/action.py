from enums.element import Element


class Action:

    def __init__(self, element):
        self.element = element

    def action(self, enum_ordinal, labyrinth):
        (x, y) = (labyrinth.robot.x + enum_ordinal.x, labyrinth.robot.y + enum_ordinal.y)

        if (x, y) in self.element:
            self.update(x, y, labyrinth)
            return True
        else:
            return False


class Build(Action):

    @staticmethod
    def update(x, y, labyrinth):
        labyrinth.walls.append((x, y))
        labyrinth.doors.remove((x, y))
        labyrinth.grid[x][y] = Element.WALL.value


class Drill(Action):

    @staticmethod
    def update(x, y, labyrinth):
        labyrinth.walls.remove((x, y))
        labyrinth.doors.append((x, y))
        labyrinth.grid[x][y] = Element.DOOR.value
