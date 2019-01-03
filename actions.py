from textwrap import dedent
from sys import exit
import plant as p
import building as b
import commands as c
import player
import messages as m

def bright_room_decisions( room, action ):
    """when the room is lit, these are the available decisions:"""

    #door actions
    if action in [x for v in c.door_actions.values() for x in v]:
        return room.get_next_room( action )

    #window actions
    elif action in c.window_actions:
        room.window_actions( action )
        return room.name

    #act on special room features
    elif action in room.action:
        room.room_feature()
        return room.name

    #add room item to inventory
    elif action in room.inventory_action:
        room.room_inventory_feature()
        return room.name

    #use inventory
    elif action in [x for value in c.inventory_actions.values() for x in value]:
        player.player.inventory_action( action )
        return room.name

    #act on plant
    elif action in c.plant_actions:
        print("\n\nThe plants wiggle under your touch.\n")
        return room.name

    else:
        print(dedent(
        """
        I don't understand. Please type again.
        """
        ))
        return room.name

def dark_room_decisions( room, action ):
    """when the room is dark, these are the available decisions:"""

    #open window shutters
    if action in c.window_actions:
        room.window_actions( action )
        return room.name

    #use flashlight
    elif action == "flashlight":
        player.player.inventory_action( action )
        return room.name

    else:
        print(m.bumble_text)
        return room.name

def room_decisions( room ):
    action = ''

    while action != 'quit':

        #is the room lit?
        if room.window == "open" or player.player.flashlight == "on":
            light = "yes"
        else:
            light = "no"

        while light == "no":
            #display dark room message
            print(m.dark_text)
            #ask for decision
            action = input("What do you want to do?\n(enter quit to end game)\n> ")
            return dark_room_decisions( room, action )

        while light == "yes":
            if room.window == "open":
                print(m.light_text)
            if player.player.flashlight == "on":
                print(m.flashlight_text)
            #display room intro message
            print(getattr(room, "message", m.filler_text))
            #display available doors to other rooms
            room.print_doors()
            #ask for decision
            action = input("What do you want to do?\n(enter quit to end game)\n> ")
            return bright_room_decisions( room, action )

    if action == "quit":
        print("You quit the game. Goodbye!")
        exit(1)
    else:
        print("you shouldn't be here")
