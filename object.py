'''
This class is here to randomize the object dispatch.
'''
import random


class Object:

    def __init__(self, ord, abs, char):
        self.ord = ord
        self.abs = abs
        self.char = char

    def object_dispatch(self, display_map):
        while display_map[self.ord][self.abs] != 'X':
            self.ord = random.randint(1,13)
            self.abs = random.randint(1,13)
        display_map[self.ord][self.abs] = self.char
        return display_map
