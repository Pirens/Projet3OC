'''
This is the basic moves of MacGyver.
In the init function, we declared 2 variables for the location of the character.
The  next functions are the basic moves on the possibles path.
'''


class Macgyver:

    def __init__(self, ord, abs):
        self.ord = ord
        self.abs = abs

    def right(self, display_map): #move right
        if display_map[self.ord][self.abs + 1] == 'O':
            return display_map
        else:
            display_map[self.ord][self.abs] = 'X'
            self.abs = self.abs + 1
            display_map[self.ord][self.abs] = 'P'
            position = display_map[self.ord][self.abs]
            return display_map

    def left(self, display_map): #move left
        if display_map[self.ord][self.abs - 1] == 'O':
            return display_map
        else:
            display_map[self.ord][self.abs] = 'X'
            self.abs = self.abs - 1
            display_map[self.ord][self.abs] = 'P'
            position = display_map[self.ord][self.abs]
            return display_map

    def up(self, display_map): #move up
        if display_map[self.ord - 1][self.abs] == 'O':
            return display_map
        else:
            display_map[self.ord][self.abs] = 'X'
            self.ord = self.ord - 1
            display_map[self.ord][self.abs] = 'P'
            position = display_map[self.ord][self.abs]
            return display_map

    def down(self, display_map): #move down
        if display_map[self.ord + 1][self.abs] == 'O':
            return display_map
        else:
            display_map[self.ord][self.abs] = 'X'
            self.ord = self.ord + 1
            display_map[self.ord][self.abs] = 'P'
            position = display_map[self.ord][self.abs]
            return display_map
