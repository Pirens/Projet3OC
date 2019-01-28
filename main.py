''' Local import '''
from display import Display
from macgyver import Macgyver
from object import Object


class Main:


    def __init__(self):
        '''Opening instances we need to play, and dispatch objects'''

        self.display = Display()
        self.character = Macgyver(1,1)
        self.needle = Object(1,1,'N')
        self.display.mapf = self.needle.object_dispatch(self.display.mapf)
        self.tube = Object(1,1,'T')
        self.display.mapf = self.tube.object_dispatch(self.display.mapf)
        self.ether = Object(1,1,'E')
        self.display.mapf = self.ether.object_dispatch(self.display.mapf)


    def play(self):

        for affichage in self.display.mapf:
            for points in affichage:
                print(points, end =" ")
            print("")
        nbr_objects = 0
        while self.display.mapf[self.character.ord][self.character.abs] != self.display.mapf[13][13]:
            print("Can you help MacGyver to asleep the guardian ?")
            print("You can use D for right, Q for left, Z for up and S for down")
            user_entry = input()

            # move right + checking if an object is a the position before
            if user_entry == 'D':
                if (self.display.mapf[self.character.ord][self.character.abs + 1] == 'N')\
                or (self.display.mapf[self.character.ord][self.character.abs + 1] == 'T')\
                or (self.display.mapf[self.character.ord][self.character.abs + 1] == 'E'):
                    nbr_objects = nbr_objects + 1
                self.display.mapf = self.character.right(self.display.mapf)

            # move left + checking if an object is a the position before
            elif user_entry == 'Q':
                if (self.display.mapf[self.character.ord][self.character.abs - 1] == 'N')\
                or (self.display.mapf[self.character.ord][self.character.abs - 1] == 'T')\
                or (self.display.mapf[self.character.ord][self.character.abs - 1] == 'E'):
                    nbr_objects = nbr_objects + 1
                self.display.mapf = self.character.left(self.display.mapf)

            # move up + checking if an object is a the position before
            elif user_entry == 'Z':
                if (self.display.mapf[self.character.ord - 1][self.character.abs] == 'N')\
                or (self.display.mapf[self.character.ord - 1][self.character.abs] == 'T')\
                or (self.display.mapf[self.character.ord - 1][self.character.abs] == 'E'):
                    nbr_objects = nbr_objects + 1
                self.display.mapf = self.character.up(self.display.mapf)

            # move down + checking if an object is a the position before
            elif user_entry == 'S':
                if (self.display.mapf[self.character.ord + 1][self.character.abs] == 'N')\
                or (self.display.mapf[self.character.ord + 1][self.character.abs] == 'T')\
                or (self.display.mapf[self.character.ord + 1][self.character.abs] == 'E'):
                    nbr_objects = nbr_objects + 1
                self.display.mapf = self.character.down(self.display.mapf)

            # in case of a wrong caracter
            else:
                print("Wrong entry!")

            # return map every time
            for affichage in self.display.mapf:
                for points in affichage:
                    print(points, end =" ")
                print("")

        '''End of the game'''
        # end of the game
        if nbr_objects == 3:
            print("You win this game")
        else:
            print("You die idiot")

main = Main()
main.play()
