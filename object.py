import random


class Object:

    ''' Initialize the coordinates and the char '''
    def __init__(self, ord, abs, char):
        self.ord = ord
        self.abs = abs
        self.char = char

    ''' Randomize the location of the object '''
    def object_dispatch(self, display_map):
        while display_map[self.ord][self.abs] != 'X':
            self.ord = random.randint(1, 13)
            self.abs = random.randint(1, 13)
        display_map[self.ord][self.abs] = self.char
        return display_map
