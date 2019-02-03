import json
import pygame
from pygame.locals import *

from object import Object
from macgyver import Macgyver

class Display:

    def __init__(self):
        with open('map.json', 'r') as f:
            self.mapf = json.load(f)
            pygame.init()
            self.needle = Object(1,1,'N')
            self.mapf = self.needle.object_dispatch(self.mapf)
            self.tube = Object(1,1,'T')
            self.mapf = self.tube.object_dispatch(self.mapf)
            self.ether = Object(1,1,'E')
            self.mapf = self.ether.object_dispatch(self.mapf)


    def display_map(self):
        window = pygame.display.set_mode((600,600), RESIZABLE)
        line_index = 0
        ord = 0
        for line in self.mapf:
            # Read char in lines
            char_index = 0
            abs = 0
            for char in line:
                # Display a sprite in function of a wall or a tile
                if self.mapf[char_index][line_index] == 'O':
                    sprite_w = pygame.image.load("ressources/wall.png").convert()
                    window.blit(sprite_w, (ord,abs))
                else:
                    sprite_t = pygame.image.load("ressources/tile.png").convert()
                    window.blit(sprite_t, (ord,abs))
                    # Ojects and characters picture on tile
                    if self.mapf[char_index][line_index] == 'G':
                        picture = pygame.image.load("ressources/gardien.png").convert_alpha()
                        window.blit(picture, (ord,abs))
                    elif self.mapf[char_index][line_index] == 'N':
                        picture = pygame.image.load("ressources/aiguille.png").convert_alpha()
                        window.blit(picture, (ord,abs))
                    elif self.mapf[char_index][line_index] == 'T':
                        picture = pygame.image.load("ressources/tube_plastique.png").convert()
                        picture.set_colorkey((255,255,255))
                        window.blit(picture, (ord,abs))
                    elif self.mapf[char_index][line_index] == 'E':
                        picture = pygame.image.load("ressources/ether.png").convert()
                        picture.set_colorkey((1,1,1))
                        window.blit(picture, (ord,abs))
                    elif self.mapf[char_index][line_index] == 'P':
                        character = pygame.image.load("ressources/macgyver.png").convert_alpha()
                        window.blit(character, (ord,abs))
                abs = abs + 40
                char_index = char_index + 1
            ord = ord + 40
            line_index = line_index + 1
        pygame.display.flip()
