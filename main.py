# Help MacGyver to escape

# Brut mapping
map = [
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]

# Starting position, to be random in the future
ord = 0
abs = 0
map[ord][abs] = 'P'

# loop of entry, actually, the end of the game is is the down-right corner
while map[ord][abs] != map[14][14]:
    print("Hi, the goal is to go down-right of this map !")
    print("You can use R, for right, L for left, U for up and D for down")
    user_entry = input()

# move right
    if user_entry == 'R':
        map[ord][abs] = 'X'
        abs = abs + 1
        map[ord][abs] = 'P'
        position = map[ord][abs]

# move left
    elif user_entry == 'L':
        map[ord][abs] = 'X'
        abs = abs - 1
        map[ord][abs] = 'P'
        position = map[ord][abs]

# move up
    elif user_entry == 'U':
        map[ord][abs] = 'X'
        ord = ord - 1
        map[ord][abs] = 'P'
        position = map[ord][abs]

# move down
    elif user_entry == 'D':
        map[ord][abs] = 'X'
        ord = ord + 1
        map[ord][abs] = 'P'
        position = map[ord][abs]
# in case of a wrong caracter
    else:
        print("Wrong caracter!")
# return map every time
    print(map)

print("You are a hero!")

# Comment bloquer les déplacements en dehors du labyrinthe
