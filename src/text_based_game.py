"""Project Two starter for the student's text-based adventure game."""

# Dante Robinson
# IT-140 Project Two
# Space Rescue Mission Text Adventure Game

def show_instructions():
    """Display game instructions."""
    print("\nSpace Rescue Mission")
    print("Collect all 7 items before confronting NEXUS.")
    print("Move commands: go north, go south, go east, go west")
    print("Item command: get <item name>")
    print("-" * 50)


def show_status(current_room, inventory, rooms):
    """Display player status."""
    print("\n------------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see a", rooms[current_room]["item"])

    print("------------------------")


def main():
    # Dictionary containing rooms, directions, and items
    rooms = {
        "Docking Bay": {
            "north": "Engineering Lab",
            "east": "Storage Room",
            "west": "Crew Quarters"
        },

        "Engineering Lab": {
            "north": "Command Center",
            "south": "Docking Bay",
            "east": "Medical Bay",
            "west": "Research Lab",
            "item": "Repair Kit"
        },

        "Command Center": {
            "south": "Engineering Lab",
            "item": "Access Card"
        },

        "Medical Bay": {
            "west": "Engineering Lab",
            "item": "Med Pack"
        },

        "Research Lab": {
            "east": "Engineering Lab",
            "item": "Navigation Chip"
        },

        "Crew Quarters": {
            "north": "Research Lab",
            "south": "Security Office",
            "east": "Docking Bay",
            "item": "Oxygen Tank"
        },

        "Security Office": {
            "north": "Crew Quarters",
            "east": "AI Core",
            "item": "Security Badge"
        },

        "Storage Room": {
            "west": "Docking Bay",
            "east": "AI Core",
            "item": "Energy Cell"
        },

        "AI Core": {
            "west": "Security Office"
        }
    }

    # Starting location and inventory
    current_room = "Docking Bay"
    inventory = []

    # Number of items needed to win
    total_items = 7

    show_instructions()

    # Main game loop
    while True:

        show_status(current_room, inventory, rooms)

        # Check for villain encounter
        if current_room == "AI Core":

            if len(inventory) == total_items:
                print("\nCongratulations!")
                print("You collected all items, repaired the shuttle,")
                print("defeated NEXUS, and escaped successfully!")
                print("Thanks for playing!")
                break

            else:
                print("\nNEXUS has detected you!")
                print("You entered the AI Core before collecting")
                print("all of the required equipment.")
                print("GAME OVER!")
                print("Thanks for playing!")
                break

        command = input("\nEnter your move: ").lower().split()

        # Handle movement commands
        if len(command) == 2 and command[0] == "go":

            direction = command[1]

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You cannot go that way!")

        # Handle item collection
        elif len(command) >= 2 and command[0] == "get":

            item_name = " ".join(command[1:])

            if ("item" in rooms[current_room] and
                    item_name.lower() == rooms[current_room]["item"].lower()):

                inventory.append(rooms[current_room]["item"])

                print(rooms[current_room]["item"],
                      "added to inventory.")

                del rooms[current_room]["item"]

            else:
                print("That item is not in this room.")

        # Invalid command
        else:
            print("Invalid command.")
            print("Use: go north/south/east/west")
            print("Or: get <item name>")


# Run the game
main()
