from textwrap import dedent

import commands as c
import messages as m

class Player( object ):

    def __init__( self ):
        self.inventory = []
        self.flashlight = "off"

    def inventory_action( self, action ):
        for tool, value in c.inventory_actions.items():
            if action in value and tool in self.inventory:
                self.request_tool( tool, action )
            else:
                pass

    def request_tool( self, tool, action ):
        if tool == "flashlight":
            self.use_flashlight( action )
        if tool == "paper":
            self.use_paper( action )

    def use_flashlight( self, action ):
        if action in c.flashlight_on_actions:
            if self.flashlight == "on":
                print("\nThe flashlight is already", self.flashlight)
            elif self.flashlight == "off":
                self.flashlight = "on"
                print(m.turn_on_flashlight_text)

        elif action in c.flashlight_off_actions:
            if self.flashlight == "on":
                print("\nYou turn off the flashlight.")
                self.flashlight = "off"
            elif self.flashlight == "off":
                print("\nThe flashlight is already", self.flashlight)

        else:
            error(1)

    def use_paper( self, action ):
        print(m.note_room_paper)

    def add_to_inventory( self, item ):
        if item not in self.inventory:
            self.inventory.append( item )
            print(f"\nYou put the {item} in your bag.")

player = Player()
