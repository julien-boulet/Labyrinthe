class Robot:

    """ j'aurai pu utiliser un tuple a la place de cette classe"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, enum_ordinal):
        self.x = self.x + enum_ordinal.x
        self.y = self.y + enum_ordinal.y
