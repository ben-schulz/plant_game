from textwrap import dedent

#>---- commands used in this file
door_actions = { #N, E, S, W
    "north": ["north", "north door", "open north door", "open north", "door north", "enter north door"],
    "east": ["east", "east door", "open east door", "open east", "door east", "enter east door"],
    "south": ["south", "south door", "open south door", "open south", "door south", "go to south door", "enter south door"],
    "west": ["west", "west door", "open west door", "open west", "door west", "go to west door", "enter west door"]
}

window_on_actions = ["window", "windows","shutters", "shutter", "open windows",  "open shutters", "open window", "open shutter", "window open", "windows open"]

window_close_actions = ["window", "windows","shutters", "shutter", "close windows","close shutters", "close window", "close shutter", "window close", "shutter close", "shutters close"]

window_actions = window_on_actions + window_close_actions

plant_actions = ["plant", "touch plant", "pull plant", "move plant"]

paper_actions = ["paper", "read", "read paper", "pick up paper", "pick up", "get paper"]

flashlight_actions = ["flashlight", "take flashlight", "get flashlight", "pick up flashlight"]

inventory_actions = {
    "flashlight": flashlight_actions,
    "paper": paper_actions,
}


#>---- text files used in this file go here
open_window = dedent(
"""
You throw open the shutters.
Light bursts into the room."""
)

close_window = dedent(
"""
You shutter the windows."""
)

no_door = "\nThere is no door here\n"

bumble_text = dedent(
"""
You bumble about in this room.
It's too dark."""
)

dark_text = dedent(
"""
The room is dark. You can't see a thing.
A silver of light spills through closed window shutters.
You think you can open them.
""")

light_text = dedent(
"""
The window shutters flap against a light breeze.
The leaves unfurl and expand under the strong sunlight."""
)

flashlight_text = "You scan the room with your flashlight."

filler_text = "\nDangling plant roots brush by your face, as if wishing you death."

not_understand = dedent(
"""
I don't understand. Please type again.
"""
)
#>---- main file
class Room( object ):
    def __init__( self, room_attr ):
        for key in room_attr:
            setattr( self, key, room_attr[key] )

    def print_doors( self ):
        doors = ", ".join(list(self.doors.keys()))
        print("This room has doors to the", doors, "\n")

    def get_next_room( self, action, door_action ):
        for direction, action_terms in door_action.items():
            if action in action_terms:
                return self.doors.get(direction, None)

    def close_window( self ):
        self.window = "closed"
        print(close_window)

    def open_window( self ):
        self.window = "open"
        print(open_window)

    def already_closed( self ):
        print("The shutters are already closed.")

    def already_open( self ):
        print("The shutters are already open.")

    def room_feature( self ):
        feature_exist = getattr(self, "feature", None)
        if feature_exist:
            if self.feature == "on":
                print(self.harm_plant_message)
                self.feature = "off"
                self.message = self.harm_plant_room_message
                return "wither"
            if self.feature == "off":
                print(self.help_plant_message)
                self.feature = "on"
                self.message = self.help_plant_room_message
                return "grow"
        else:
            pass


    def room_inventory_feature( self ):
        inventory_feature_exist = getattr(self, "inventory_feature", None)
        if inventory_feature_exist:
            if self.inventory_feature == "exist":
                print(self.inventory_message)
                self.message = self.inventory_taken_message
                self.inventory_feature = "not_exist"
                return "taken"
            if self.inventory_feature == "not_exist":
                print(self.no_item_message)
                return "nothing"
        else:
            pass


    def bright_room_decisions( self, action, plant, player ):
        """when the room is lit, these are the available decisions:"""

        #door actions
        if action in [x for v in door_actions.values() for x in v]:
            next_room = self.get_next_room( action, door_actions )
            if next_room == None:
                print(no_door)
                next_room = self.name
            else:
                plant.grow_and_report()
            return next_room

        #window actions
        elif action in window_on_actions:
            self.already_open()
            return self.name

        elif action in window_close_actions:
            self.close_window()
            plant.decrease_growth_rate_and_report()
            return self.name

        #act on special room features
        elif action in self.action:
            plant_command = self.room_feature()
            if plant_command == "wither":
                plant.wither_and_report()
                return self.name
            elif plant_command == "grow":
                plant.grow_and_report()
                return self.name

        #add room item to inventory
        elif action in self.inventory_action:
            if self.room_inventory_feature() == "taken":
                player.add_to_inventory( self.inventory_item )
            else:
                pass
            return self.name

        #use inventory
        elif action in [x for value in inventory_actions.values() for x in value]:
            for tool, value in inventory_actions.items():
                if action in value and tool in player.inventory:
                    player.request_tool( tool, action )
                else:
                    pass
            return self.name

        #act on plant
        elif action in plant_actions:
            print("\n\nThe plants wiggle under your touch.\n")
            return self.name

        else:
            print( not_understand )
            return self.name

    def dark_room_decisions( self, action, plant, player ):

        #window actions
        if action in window_on_actions:
            self.open_window()
            plant.increase_growth_rate_and_report()
            return self.name

        elif action in window_close_actions:
            self.already_closed()
            return self.name

        #use flashlight
        elif "flashlight" in action:
            player.use_flashlight( action )
            return self.name

        else:
            print(bumble_text)
            return self.name

    def room_decisions( self, plant, player ):
        action = ''

        while action != 'quit':

            #is the room lit?
            if self.window == "open" or player.flashlight == "on":
                light = "yes"
            else:
                light = "no"

            while light == "no":
                #display dark room message
                print( dark_text )
                #ask for decision
                action = input("What do you want to do?\n(enter quit to end game)\n> ")
                return self.dark_room_decisions( action, plant, player )

            while light == "yes":
                #display light conditions
                if self.window == "open":
                    print( light_text )
                if player.flashlight == "on":
                    print( flashlight_text )
                #display room intro message
                print(getattr(self, "message", filler_text))
                #display available doors to other rooms
                self.print_doors()
                #ask for decision
                action = input("What do you want to do?\n(enter quit to end game)\n> ")
                return self.bright_room_decisions( action, plant, player )

        if action == "quit":
            print("You quit the game. Goodbye!")
            exit(1)
        else:
            error(1)
