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
needle = Object(1,1)
tube = Object(1,1)
ether = Object(1,1)

'''Objects integration on the map'''
# Objects integration on the map

display_map = needle.object_dispatch(display_map)
display_map.map[needle.ordo][needle.abso] = 'N'
display_map = tube.object_dispatch(display_map)
display_map.map[tube.ordo][tube.abso] = 'T'
display_map = ether.object_dispatch(display_map)
display_map.map[ether.ordo][ether.abso] = 'E'

'''Have a look at the beginning map'''
for affichage in display_map.map:
    for points in affichage:
        print(points, end =" ")
    print("")

'''Object variable'''
nbr_objects = 0

'''Gaming session'''
# loop of move if the character isn't on the ending poition
while display_map.map[character.ord][character.abs] != display_map.map[13][13]:
    print("Can you help MacGyver to asleep the guardian ?")
    print("You can use D for right, Q for left, Z for up and S for down")
    user_entry = input()

    # move right + checking if an object is a the position before
    if user_entry == 'D':
        if (display_map.map[character.ord][character.abs + 1] == 'N')\
        or (display_map.map[character.ord][character.abs + 1] == 'T')\
        or (display_map.map[character.ord][character.abs + 1] == 'E'):
            nbr_objects = nbr_objects + 1
        display_map = character.right(display_map)

    # move left + checking if an object is a the position before
    elif user_entry == 'Q':
        if (display_map.map[character.ord][character.abs - 1] == 'N')\
        or (display_map.map[character.ord][character.abs - 1] == 'T')\
        or (display_map.map[character.ord][character.abs - 1] == 'E'):
            nbr_objects = nbr_objects + 1
        display_map = character.left(display_map)

    # move up + checking if an object is a the position before
    elif user_entry == 'Z':
        if (display_map.map[character.ord - 1][character.abs] == 'N')\
        or (display_map.map[character.ord - 1][character.abs] == 'T')\
        or (display_map.map[character.ord - 1][character.abs] == 'E'):
            nbr_objects = nbr_objects + 1
        display_map = character.up(display_map)

    # move down + checking if an object is a the position before
    elif user_entry == 'S':
        if (display_map.map[character.ord + 1][character.abs] == 'N')\
        or (display_map.map[character.ord + 1][character.abs] == 'T')\
        or (display_map.map[character.ord + 1][character.abs] == 'E'):
            nbr_objects = nbr_objects + 1
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
if nbr_objects == 3:
    print("You win this game")
else:
    print("You die idiot")

# Comment bloquer les déplacements en dehors du labyrinthe
