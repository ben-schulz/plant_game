from textwrap import dedent

import room_attr as r
import commands as c
import messages as m

class Room( object ):
    def __init__( self, room_attr ):
        for key in room_attr:
            setattr( self, key, room_attr[key] )

    def print_doors( self ):
        doors = ", ".join(list(self.doors.keys()))
        print("This room has doors to the", doors, "\n")

    def get_next_room( self, action ):
        for direction, action_terms in c.door_actions.items():
            if action in action_terms:
                return self.doors.get(direction, None)

    def close_window( self ):
        self.window = "closed"
        print(m.close_window)

    def open_window( self ):
        self.window = "open"
        print(m.open_window)

    def already_closed( self ):
        print("The shutters are already closed.")

    def already_open( self ):
        print("The shutters are already open.")

    def room_feature( self ):
        if self.feature:
            print(self.harm_plant_message)
            self.feature = False
            self.message = self.harm_plant_room_message
            return "wither"

        if self.feature == False:
            print(self.help_plant_message)
            self.feature = True
            self.message = self.help_plant_room_message
            return "grow"

    def room_inventory_feature( self ):
        if self.inventory_feature:
            print(self.inventory_message)
            self.message = self.inventory_taken_message
            self.inventory_feature = False
            return "taken"

        elif self.inventory_feature == False:
            print(self.no_item_message)
            return "nothing"

def check_room( room ):
    if room == "death":
        return True
    elif room == "exit":
        return True
    else:
        return False

rooms = {
    "note_room": Room( r.note_room_attr ),
    "water_room": Room( r.water_room_attr ),
    "heat_room": Room( r.heat_room_attr ),
    "room_with_exit": Room( r.room_with_exit_attr ),
    "symbiont_room": Room( r.symbiont_room_attr ),
    "east_note_room": Room( r.east_note_room_attr ),
    "west_note_room": Room( r.west_note_room_attr ),
    "flashlight_room": Room( r.flashlight_room_attr ),
}
