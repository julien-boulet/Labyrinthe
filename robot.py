class Robot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, letter):
        if letter == 'N':
            self.x = self.x - 1
        elif letter == 'S':
            self.x = self.x + 1
        elif letter == 'O':
            self.y = self.y - 1
        elif letter == 'E':
            self.y = self.y + 1
