# Function import
import random

'''Class for the 3 objects you need to get high the guardian'''
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
