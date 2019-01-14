# Local import
from map import Map


'''Your hero'''
class Macgyver:

    '''Init'''
    def __init__(self, ord, abs):
        self.ord = ord
        self.abs = abs

    '''Move right'''
    def right(self, display_map):
        if display_map.map[self.ord][self.abs + 1] == 'O': #If it's a wall, you can't move
            return display_map
        else:
            display_map.map[self.ord][self.abs] = 'X'
            self.abs = self.abs + 1
            display_map.map[self.ord][self.abs] = 'P'
            position = display_map.map[self.ord][self.abs]
            return display_map

    '''Move left'''
    def left(self, display_map):
        if display_map.map[self.ord][self.abs - 1] == 'O': #If it's a wall, you can't move
            return display_map
        else:
            display_map.map[self.ord][self.abs] = 'X'
            self.abs = self.abs - 1
            display_map.map[self.ord][self.abs] = 'P'
            position = display_map.map[self.ord][self.abs]
            return display_map

    '''Move up'''
    def up(self, display_map):
        if display_map.map[self.ord - 1][self.abs] == 'O': #If it's a wall, you can't move
            return display_map
        else:
            display_map.map[self.ord][self.abs] = 'X'
            self.ord = self.ord - 1
            display_map.map[self.ord][self.abs] = 'P'
            position = display_map.map[self.ord][self.abs]
            return display_map

    '''Move down'''
    def down(self, display_map):
        if display_map.map[self.ord + 1][self.abs] == 'O': #If it's a wall, you can't move
            return display_map
        else:
            display_map.map[self.ord][self.abs] = 'X'
            self.ord = self.ord + 1
            display_map.map[self.ord][self.abs] = 'P'
            position = display_map.map[self.ord][self.abs]
            return display_map
