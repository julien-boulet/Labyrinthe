from labyrinth import *


class Map:

    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.labyrinth = Labyrinth.read_content(content)

    def __repr__(self):
        return "<Map {}>".format(self.name)