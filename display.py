'''
Here, you will find the map generation. First of all,
the init part open the json file and wil randomly generate 3 objects.
After, the display_map will display the map after every moves.
'''

import json
import pygame
from pygame.locals import *

from object import Object
from macgyver import Macgyver


class Display:

    def __init__(self): #init the map in mapf and dispatch the 3 objects
        with open('map.json', 'r') as f:
            self.map = json.load(f)
            pygame.init()
            self.needle = Object(1,1,'N')
            self.map = self.needle.object_dispatch(self.map)
            self.tube = Object(1,1,'T')
            self.map = self.tube.object_dispatch(self.map)
            self.ether = Object(1,1,'E')
            self.map = self.ether.object_dispatch(self.map)

    def display_map(self): #display map
        window = pygame.display.set_mode((600,600))
        line_index, ord = 0, 0
        for line in self.map:
            char_index, abs = 0, 0
            for char in line:
                if self.map[char_index][line_index] == 'O':
                    sprite_w = pygame.image.load("ressources/wall.png").convert()
                    window.blit(sprite_w, (ord,abs))
                else:
                    sprite_t = pygame.image.load("ressources/tile.png").convert()
                    window.blit(sprite_t, (ord,abs))
                    if self.map[char_index][line_index] == 'G':
                        picture = pygame.image.load("ressources/gardien.png").convert_alpha()
                        window.blit(picture, (ord,abs))
                    elif self.map[char_index][line_index] == 'N':
                        picture = pygame.image.load("ressources/aiguille.png").convert_alpha()
                        window.blit(picture, (ord,abs))
                    elif self.map[char_index][line_index] == 'T':
                        picture = pygame.image.load("ressources/tube_plastique.png").convert()
                        picture.set_colorkey((255,255,255))
                        window.blit(picture, (ord,abs))
                    elif self.map[char_index][line_index] == 'E':
                        picture = pygame.image.load("ressources/ether.png").convert()
                        picture.set_colorkey((1,1,1))
                        window.blit(picture, (ord,abs))
                    elif self.map[char_index][line_index] == 'P':
                        character = pygame.image.load("ressources/macgyver.png").convert_alpha()
                        window.blit(character, (ord,abs))
                char_index, abs =char_index + 1,  abs + 40
            line_index, ord = line_index + 1, ord + 40
        pygame.display.flip()
