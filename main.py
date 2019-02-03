import pygame
from pygame.locals import *
''' Local import '''
from display import Display
from macgyver import Macgyver
from object import Object


class Main:


    def __init__(self):
        '''Opening instances we need to play, and dispatch objects'''

        self.display = Display()
        self.character = Macgyver(1,1)

    def play(self):

        self.display.display_map()
        nbr_objects = 0
        while self.display.mapf[self.character.ord][self.character.abs] != self.display.mapf[13][13]:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.display.mapf[self.character.ord][self.character.abs] = self.display.mapf[13][13]
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        if (self.display.mapf[self.character.ord][self.character.abs + 1] == 'N')\
                        or (self.display.mapf[self.character.ord][self.character.abs + 1] == 'T')\
                        or (self.display.mapf[self.character.ord][self.character.abs + 1] == 'E'):
                            nbr_objects = nbr_objects + 1
                        self.display.mapf = self.character.right(self.display.mapf)
                    if event.key == K_LEFT:
                        if (self.display.mapf[self.character.ord][self.character.abs - 1] == 'N')\
                        or (self.display.mapf[self.character.ord][self.character.abs - 1] == 'T')\
                        or (self.display.mapf[self.character.ord][self.character.abs - 1] == 'E'):
                            nbr_objects = nbr_objects + 1
                        self.display.mapf = self.character.left(self.display.mapf)
                    if event.key == K_UP:
                        if (self.display.mapf[self.character.ord - 1][self.character.abs] == 'N')\
                        or (self.display.mapf[self.character.ord - 1][self.character.abs] == 'T')\
                        or (self.display.mapf[self.character.ord - 1][self.character.abs] == 'E'):
                            nbr_objects = nbr_objects + 1
                        self.display.mapf = self.character.up(self.display.mapf)
                    if event.key == K_DOWN:
                        if (self.display.mapf[self.character.ord + 1][self.character.abs] == 'N')\
                        or (self.display.mapf[self.character.ord + 1][self.character.abs] == 'T')\
                        or (self.display.mapf[self.character.ord + 1][self.character.abs] == 'E'):
                            nbr_objects = nbr_objects + 1
                        self.display.mapf = self.character.down(self.display.mapf)
                    self.display.display_map()

        '''End of the game'''
        # end of the game
        if nbr_objects == 3:
            print("You win this game")
        else:
            print("You die idiot")

main = Main()
main.play()
