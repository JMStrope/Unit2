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
last_movement = ''

#game loop
game_over = False
while game_over == False:
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
    elif location == 'stairs down':
        print("You see a stair case leading back down")

    elif location == 'prize':
        print("You have successfully cleared the dungeon. Your prize is $1,000,000,000")
        break
    #player choices
    player_input = input("What would you like to do? (Left, Right, Up, Down, Grab, Fight, Inventory) > ")
    if player_input == 'Right' :
        last_movement = 'Right'
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
        if location == 'monster':
            if 'sword' in inventory:
                print("You defeated the Big Monster")
                print("But your sword was destroyed in the fight")
                inventory.remove('sword')
                dungeon[current_floor][current_room] = 'empty'
            else: 
                ("You tried to fight a big monster without a weapon.")
                game_over = True 
        elif location == 'boss monster':
            if 'sword' in inventory and 'magic stones' in inventory:
                print("You defeated the Dungeons Boss Monster, Congratulations. You may now collect your prize and escape the Dungeon")
                dungeon[current_floor][current_room] = 'empty'
            else:
                print("You fought the Boss Monster without the necessary equipment. YOU DIED")
                game_over = True
        else:
            print("There are no monsters to fight")
    if location == 'monster' or 'boss monster' and player_input: pass

    #Play again
    if game_over == True:
        player_input = input("Would you like to play again? (y/n)")
        if player_input == 'y':
            game_over = False
        else:
            break
        
    

            

