import pygame
from pygame.locals import *

from display import Display  # display is used to display the map
from macgyver import Macgyver  # macgyver is used to move the character


class Main:

    ''' Initialize display and macgyver '''
    def __init__(self):  # initialize the map and Macgyver location
        self.display = Display()
        self.char = Macgyver(1, 1, 0)

    ''' Let's play '''
    def play(self, nbr_objects):  # play with Macgyver
        self.display.display_map()
        while self.display.map[self.char.ord][self.char.abs]\
                != self.display.map[13][13]:
            for event in pygame.event.get():
                if event.type == QUIT:  # to quit the game
                    self.display.map[self.char.ord][self.char.abs]\
                            = self.display.map[13][13]
                if event.type == KEYDOWN:  # moving time
                    if event.key == K_RIGHT:
                        self.display.map = self.char.right(self.display.map)
                    if event.key == K_LEFT:
                        self.display.map = self.char.left(self.display.map)
                    if event.key == K_UP:
                        self.display.map = self.char.up(self.display.map)
                    if event.key == K_DOWN:
                        self.display.map = self.char.down(self.display.map)
                self.display.display_map()
        if self.char.nbr_objects == 3:  # if you have all the necessary objects
            print("You win this game")
        else:  # if not
            print("You die idiot")


main = Main()
main.play(0)
