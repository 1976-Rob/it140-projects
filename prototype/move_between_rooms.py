"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# move_between_rooms.py
# IT-140 Milestone: Moving Between Rooms
# This program allows a player to move between rooms
# in a simplified dragon text game or exit the game.

# A dictionary for the simplified dragon text game.
# The dictionary links rooms to other rooms.
rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}

# Start the player in the Great Hall
current_room = 'Great Hall'

# Gameplay loop
while current_room != 'exit':

    # Display the current room
    print('\nYou are in the', current_room)

    # Get player command
    command = input('Enter a command (go north, go south, go east, go west, or exit): ')

    # Exit command
    if command.lower() == 'exit':
        current_room = 'exit'

    # Move command
    elif command.startswith('go '):
        direction = command[3:].lower()

        # Check whether the direction is valid from the current room
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            print('You move', direction + '.')
        else:
            print('Invalid direction! You cannot go that way.')

    # Invalid command
    else:
        print('Invalid command! Please enter a valid command.')

# End of game
print('\nThanks for playing!')

