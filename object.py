# Function import
import random

'''Class for the 3 objects you need to get high the guardian'''
class Object:

    def __init__(self, ordo, abso, char):
        self.ordo = ordo
        self.abso = abso
        self.char = char

    def object_dispatch(self, display_map):
        while display_map[self.ordo][self.abso] != 'X':
            self.ordo = random.randint(1,13)
            self.abso = random.randint(1,13)
        display_map[self.ordo][self.abso] = self.char
        return display_map
