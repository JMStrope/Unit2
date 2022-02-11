#Map of dungeon
dungeon = [
    ['prize','boss monster', 'sword', 'sword', 'stairs down'],
    ['magic stones','monster','stairs down','stairs up','empty'],
    ['empty','sword','stairs up','empty','monster']
    ]

#player info
inventory = []
current_room = 0
current_floor = 2
location = dungeon[current_floor][current_room]


#game loop
while True:

    #Update Location
    location = dungeon[current_floor][current_room]

    #Where we are
    if location == 'empty':
        print("You wake up in an empty room")
    elif location == 'sword':
        print("sword") 
    elif location == 'stairs up':
        print("You see a staircase leading upwards")
    elif location == 'empty':
        print("This room is empty")
    elif location == 'monster':
        print("You encountered a large monnster")


    #player choices
    player_input = input("What would you like to do? (Left, Right, Up, Down, Grab, Fight) >")
    if player_input == 'right':
        current_room += 1
        if current_room == 5:
            print("You cannot move any further that way")
            current_room = 4
    if player_input == 'left':
        current_room -= 1
        if current_room == -1:
            print("You cannot move any further to the left")
            current_room = 0
    if player_input == 'Up' and current_room == 2: 
        current_floor += 1 and print("You move to the next floor")
