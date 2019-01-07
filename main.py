from map import Map
from macgyver import Macgyver
from guardian import Guardian
from object import Object
# Help MacGyver to escape
display_map = Map()
# Starting position, to be random in the future
ord = 1
abs = 0

# loop of entry, actually, the end of the game is is the down-right corner
while display_map.map[ord][abs] != display_map.map[13][14]:
    print("Hi, the goal is to go down-right of this map !")
    print("You can use R, for right, L for left, U for up and D for down")
    user_entry = input()

# move right
    if user_entry == 'R':
        display_map.map[ord][abs] = 'X'
        abs = abs + 1
        display_map.map[ord][abs] = 'P'
        position = display_map.map[ord][abs]

# move left
    elif user_entry == 'L':
        display_map.map[ord][abs] = 'X'
        abs = abs - 1
        display_map.map[ord][abs] = 'P'
        position = display_map.map[ord][abs]

# move up
    elif user_entry == 'U':
        display_map.map[ord][abs] = 'X'
        ord = ord - 1
        display_map.map[ord][abs] = 'P'
        position = display_map.map[ord][abs]

# move down
    elif user_entry == 'D':
        display_map.map[ord][abs] = 'X'
        ord = ord + 1
        display_map.map[ord][abs] = 'P'
        position = display_map.map[ord][abs]
# in case of a wrong caracter
    else:
        print("Wrong caracter!")
# return map every time
    for affichage in display_map.map:
        for caracter in affichage:
            print(caracter, end =" ")
        print("")

print("You are a hero!")

# Comment bloquer les déplacements en dehors du labyrinthe
