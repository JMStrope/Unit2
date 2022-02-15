#Map of dungeon
dungeon = [
    ['prize','boss monster', 'sword', 'stairs down', 'sword'],
    ['magic stones','monster','stairs down','empty','stairs up'],
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
        print("You are in an empty room")
    elif location == 'sword':
        print("You walk into a room with a sword") 
    elif location == 'stairs up':
        print("You see a staircase leading upwards")
    elif location == 'empty':
        print("This room is empty")
    elif location == 'monster':
        print("You encountered a small monster")
    elif location == 'magic stones':
        print("You find a room with magic stones")
    elif location == 'boss monster':
        print("You have encounter the Boss monster, Defeating him will allow you to escape")
    
    #player choices
    player_input = input("What would you like to do? (Left, Right, Up, Down, Grab, Fight, Inventory) > ")
    if player_input == 'Right' :
        current_room += 1
        if current_room == 5:
            print("You cannot move any further that way")
            current_room = 4
    elif player_input == 'Left' :
        current_room -= 1
        if current_room == -1:
            print("You cannot move any further to the left")
            current_room = 0
    elif player_input == 'Up': 
        if location == 'stairs up':
            current_floor -= 1
            print("You move to the next floor")
        else:
            print("There are no stairs leading up here.")
    elif player_input == 'Down':
        if location == 'stairs down':
            current_floor += 1
        else:
            print("There are no stairs leading downwards.")
    elif player_input == 'Grab':
        if location == 'Sword' or 'Magic Stones':
            inventory.append(location)
            dungeon[current_floor][current_room] = 'empty'
        else:
            print("There is nothing to grab here")
    elif player_input == 'Inventory':
        print("you have:")
        print(' '.join(inventory))
    elif player_input == 'Fight':
        if location == 'monster' and 'sword' in inventory:
            print("You defeated the Big Monster")
            dungeon[current_floor][current_room] = 'empty'
    elif player_input == 'Fight':
        if location == 'boss monster' and ('sword' in inventory and 'magic stones' in inventory):
            print("You defeated the Dungeons Boss Monster, Congratulations. You may now escape the Dungeon")
            break
        else:
            print("There are no enemies nearby you can fight right now")

            

