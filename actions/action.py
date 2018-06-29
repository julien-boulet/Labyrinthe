from enums.element import Element


class Action:

    """ un peu tiré par les cheveux mais c'etait pour tester l'heritage"""

    def __init__(self, element):
        self.element = element

    def action(self, enum_ordinal, labyrinth):
        (x, y) = (labyrinth.robot.x + enum_ordinal.x, labyrinth.robot.y + enum_ordinal.y)

        if (x, y) in self.element:
            self.update(x, y, labyrinth)
            return True
        else:
            return False

    @staticmethod
    def update(x,y,labyrinth):
        print("update action")


class Build(Action):
    letter = 'B'

    @staticmethod
    def update(x, y, labyrinth):
        labyrinth.walls.append((x, y))
        labyrinth.doors.remove((x, y))
        labyrinth.grid[x][y] = Element.WALL.value


class Drill(Action):
    letter = 'D'

    @staticmethod
    def update(x, y, labyrinth):
        labyrinth.walls.remove((x, y))
        labyrinth.doors.append((x, y))
        labyrinth.grid[x][y] = Element.DOOR.value
