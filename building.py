from textwrap import dedent
import plant as p
import commands as c
import room_attr as r
import player
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
                next_room = self.doors.get(direction, None)
        if next_room == None:
            print(m.no_door)
            next_room = self.name
        else:
            p.plant.grow_and_report()
        return next_room

    def window_actions( self, action ):
        def close_window():
            self.window = "closed"
            print(m.close_window)

        def open_window():
            self.window = "open"
            print(m.open_window)

        if self.window == "open":
            if action in c.window_close_actions:
                close_window()
                p.plant.decrease_growth_rate_and_report()
            else:
                print("The shutters are already open.")

        elif self.window == "closed":
            if action in c.window_on_actions:
                open_window()
                p.plant.increase_growth_rate_and_report()
            else:
                print("The shutters are already closed.")
        else:
            error(1)

    def room_feature( self ):
        if self.feature:
            print(self.harm_plant_message)
            p.plant.wither_and_report()
            self.feature = False
            self.message = self.harm_plant_room_message

        elif self.feature == False:
            print(self.help_plant_message)
            p.plant.grow_and_report()
            self.feature = True
            self.message = self.help_plant_room_message
        else:
            error(1)

    def room_inventory_feature( self ):
        if self.inventory_feature:
            print(self.inventory_message)
            player.player.add_to_inventory( self.inventory_item )
            self.message = self.inventory_taken_message
            self.inventory_feature = False

        elif self.inventory_feature == False:
            print(self.no_item_message)
        else:
            error(1)

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
