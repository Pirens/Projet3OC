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
        self.character = Macgyver(1,1)

    def play(self, nbr_objects): #play with Macgyver
        self.display.display_map()
        self.nbr_objects = nbr_objects
        while self.display.map[self.character.ord][self.character.abs] != self.display.map[13][13]:
            for event in pygame.event.get():
                if event.type == QUIT: #in the case you want to quit this game
                    self.nbr_objects = 0 #you will not win like this !
                    self.display.map[self.character.ord][self.character.abs] = self.display.map[13][13]
                if event.type == KEYDOWN: #moving time
                    if event.key == K_RIGHT:
                        main.move_right()
                    if event.key == K_LEFT:
                        main.move_left()
                    if event.key == K_UP:
                        main.move_up()
                    if event.key == K_DOWN:
                        main.move_down()
                    self.display.display_map()
        if self.nbr_objects == 3: #if you take all the necessary objects
            print("You win this game")
        else: #if not
            print("You die idiot")

    def move_right(self): #object verification before moving
        if (self.display.map[self.character.ord][self.character.abs + 1] == 'N')\
        or (self.display.map[self.character.ord][self.character.abs + 1] == 'T')\
        or (self.display.map[self.character.ord][self.character.abs + 1] == 'E'):
            self.nbr_objects = self.nbr_objects + 1
        self.display.map = self.character.right(self.display.map)

    def move_left(self):  #object verification before moving
        if (self.display.map[self.character.ord][self.character.abs - 1] == 'N')\
        or (self.display.map[self.character.ord][self.character.abs - 1] == 'T')\
        or (self.display.map[self.character.ord][self.character.abs - 1] == 'E'):
            self.nbr_objects = self.nbr_objects + 1
        self.display.map = self.character.left(self.display.map)

    def move_up(self):  #object verification before moving
        if (self.display.map[self.character.ord - 1][self.character.abs] == 'N')\
        or (self.display.map[self.character.ord - 1][self.character.abs] == 'T')\
        or (self.display.map[self.character.ord - 1][self.character.abs] == 'E'):
            self.nbr_objects = self.nbr_objects + 1
        self.display.map = self.character.up(self.display.map)

    def move_down(self):  #object verification before moving
        if (self.display.map[self.character.ord + 1][self.character.abs] == 'N')\
        or (self.display.map[self.character.ord + 1][self.character.abs] == 'T')\
        or (self.display.map[self.character.ord + 1][self.character.abs] == 'E'):
            self.nbr_objects = self.nbr_objects + 1
        self.display.map = self.character.down(self.display.map)


main = Main()
main.play(0)
