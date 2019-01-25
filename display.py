import json
import pygame
from pygame.locals import *

class Display:

    def __init__(self):
        with open('map.json', 'r') as f:
            self.mapf = json.load(f)

    def display_map(self):
        for affichage in main.display.mapf:
            for points in affichage:
                print(points, end =" ")
            print("")
