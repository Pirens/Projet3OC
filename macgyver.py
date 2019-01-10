from map import Map

class Macgyver:
    # Class initialization
    def __init__(self, ord, abs):
        self.ord = ord
        self.abs = abs

    # Caracter move right
    def right(self, display_map):
        if display_map.map[self.ord][self.abs + 1] == 'O':
            return display_map
        else:
            display_map.map[self.ord][self.abs] = 'X'
            self.abs = self.abs + 1
            display_map.map[self.ord][self.abs] = 'P'
            position = display_map.map[self.ord][self.abs]
            return display_map

    # Caracter move left
    def left(self, display_map):
        if display_map.map[self.ord][self.abs - 1] == 'O':
            return display_map
        else:
            display_map.map[self.ord][self.abs] = 'X'
            self.abs = self.abs - 1
            display_map.map[self.ord][self.abs] = 'P'
            position = display_map.map[self.ord][self.abs]
            return display_map

    # Caracter move up
    def up(self, display_map):
        if display_map.map[self.ord - 1][self.abs] == 'O':
            return display_map
        else:
            display_map.map[self.ord][self.abs] = 'X'
            self.ord = self.ord - 1
            display_map.map[self.ord][self.abs] = 'P'
            position = display_map.map[self.ord][self.abs]
            return display_map

    # Carcter move down
    def down(self, display_map):
        if display_map.map[self.ord + 1][self.abs] == 'O':
            return display_map
        else:
            display_map.map[self.ord][self.abs] = 'X'
            self.ord = self.ord + 1
            display_map.map[self.ord][self.abs] = 'P'
            position = display_map.map[self.ord][self.abs]
            return display_map
