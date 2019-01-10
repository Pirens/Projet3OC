from map import Map
from macgyver import Macgyver
from object import Object
# Help MacGyver to escape
display_map = Map()
character = Macgyver(1,1)
# Starting position, to be random in the future
ord = 1
abs = 1

# loop of entry, actually, the end of the game is is the down-right corner
while display_map.map[ord][abs] != display_map.map[13][14]:
    print("Hi, the goal is to go down-right of this map !")
    print("You can use R, for right, L for left, U for up and D for down")
    user_entry = input()

# move right
    if user_entry == 'R':
        display_map = character.right(display_map)

# move left
    elif user_entry == 'L':
        display_map = character.left(display_map)

# move up
    elif user_entry == 'U':
        display_map = character.up(display_map)

# move down
    elif user_entry == 'D':
        display_map = character.down(display_map)

# in case of a wrong caracter
    else:
        print("Wrong entry!")
# return map every time
    for affichage in display_map.map:
        for points in affichage:
            print(points, end =" ")
        print("")

print("You are a hero!")

# Comment bloquer les déplacements en dehors du labyrinthe
