# Function import
import random

# Local import
from map import Map


class Object:

    def __init__(self, ordo, abso):
        self.ordo = ordo
        self.abso = abso

    def needle(self, display_map):
        while display_map.map[self.ordo][self.abso] != 'N':
            self.ordo = random.randint(1,13)
            self.abso = random.randint(1,13)
            # Need a checking, to see if the Object is on the right position
            if display_map.map[self.ordo][self.abso] == 'X':
                display_map.map[self.ordo][self.abso] = 'N'
        return display_map

    def tube(self, display_map):
        while display_map.map[self.ordo][self.abso] != 'T':
            self.ordo = random.randint(1,13)
            self.abso = random.randint(1,13)
            if display_map.map[self.ordo][self.abso] == 'X':
                display_map.map[self.ordo][self.abso] = "T"
        return display_map

    def ether(self, display_map):
        while display_map.map[self.ordo][self.abso] != 'E':
            self.ordo = random.randint(1,13)
            self.abso = random.randint(1,13)
            if display_map.map[self.ordo][self.abso] == 'X':
                display_map.map[self.ordo][self.abso] = "E"
        return display_map
