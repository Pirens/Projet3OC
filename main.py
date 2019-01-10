# Local import
from map import Map
from macgyver import Macgyver
from object import Object

'''Opening the class instance'''
# Instance of map
display_map = Map()
# Instance of Macgyver and beginning position
character = Macgyver(1,1)
# Instance of object
dispatch_objects = Object(1,1)

'''Objects integration on the map'''
# Objects integration on the map
display_map = dispatch_objects.needle(display_map)
display_map = dispatch_objects.tube(display_map)
display_map = dispatch_objects.ether(display_map)

'''Have a look to the beginning map'''
for affichage in display_map.map:
    for points in affichage:
        print(points, end =" ")
    print("")
    
'''Gaming session'''
# loop of move
while display_map.map[character.ord][character.abs] != display_map.map[13][13]:
    print("Hi, the goal is to go down-right of this map !")
    print("You can use D for right, Q for left, Z for up and S for down")
    user_entry = input()

    # move right
    if user_entry == 'D':
        display_map = character.right(display_map)

    # move left
    elif user_entry == 'Q':
        display_map = character.left(display_map)

    # move up
    elif user_entry == 'Z':
        display_map = character.up(display_map)

    # move down
    elif user_entry == 'S':
        display_map = character.down(display_map)

    # in case of a wrong caracter
    else:
        print("Wrong entry!")

    # return map every time
    for affichage in display_map.map:
        for points in affichage:
            print(points, end =" ")
        print("")

'''End of the game'''
# end of the game
print("You are a hero!")

# Comment bloquer les déplacements en dehors du labyrinthe
