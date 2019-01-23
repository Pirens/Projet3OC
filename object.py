# Function import
import random

# Local import
from map import Map

'''Class for the 3 objects you need to get high the guardian'''
class Object:

    def __init__(self, ordo, abso):
        self.ordo = ordo
        self.abso = abso

    def object_dispatch(self, display_map):
        while display_map.map[self.ordo][self.abso] != 'X':
            self.ordo = random.randint(1,13)
            self.abso = random.randint(1,13)
        return display_map
