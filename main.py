'''
This is the main part of the game. You launch it to launch the game.
The first action of the class is to initialize the map with the character location,
next, you will find the function "play", which is users interaction core.
After this, you have 4 differents functions. They are used to be the verification of an object
in a given position before moving the character.

I hope you will enjoy this first python project in Openclassroom --> Pirens
'''


import pygame
from pygame.locals import *

from display import Display #display is used to display the map
from macgyver import Macgyver #macgyver is used to move the character


class Main:

    def __init__(self): #initialize the map and Macgyver location
        self.display = Display()
        self.character = Macgyver(1,1,0)

    def play(self, nbr_objects): #play with Macgyver
        self.display.display_map()
        while self.display.map[self.character.ord][self.character.abs] != self.display.map[13][13]:
            for event in pygame.event.get():
                if event.type == QUIT: #in the case you want to quit this game
                    self.display.map[self.character.ord][self.character.abs] = self.display.map[13][13]
                if event.type == KEYDOWN: #moving time
                    if event.key == K_RIGHT:
                        self.display.map = self.character.right(self.display.map)
                    if event.key == K_LEFT:
                        self.display.map = self.character.left(self.display.map)
                    if event.key == K_UP:
                        self.display.map = self.character.up(self.display.map)
                    if event.key == K_DOWN:
                        self.display.map = self.character.down(self.display.map)
                    self.display.display_map()
        if self.character.nbr_objects == 3: #if you take all the necessary objects
            print("You win this game")
        else: #if not
            print("You die idiot")


main = Main()
main.play(0)
