from textwrap import dedent

#>--- commands used in this file go here
flashlight_on_actions = ["flashlight", "use flashlight",  "turn on flashlight", "flashlight on", "on flashlight", "open flashlight"]

flashlight_off_actions = ["turn off flashlight", "put away flashlight", "flashlight off", "off flashlight", "close flashlight", "not use flashlight"]

#>---- texts used in this file go here
turn_on_flashlight_text = dedent("""
You turn on the flashlight.
You can see the room now.
The plants are not affected by the light.
""")

note_room_paper = dedent("""
You unfold the piece of paper:

    GET OUT NOW!!!
    The experiment... the GMO symbionts are driving the growth.
    The plants are now everywhere.
    They're growing fast, sealing off doors, covering the building...
    Run! Get out of the building before it's too late!""")

#>---- main file
class Player( object ):

    def __init__( self ):
        self.inventory = []
        self.flashlight = "off"

    def request_tool( self, tool, action ):
        if tool == "flashlight":
            self.use_flashlight( action )
        if tool == "paper":
            self.use_paper( action )

    def use_flashlight( self, action ):
        if action in flashlight_on_actions:
            if self.flashlight == "on":
                print("\nThe flashlight is already", self.flashlight)
            elif self.flashlight == "off":
                self.flashlight = "on"
                print(turn_on_flashlight_text)

        elif action in flashlight_off_actions:
            if self.flashlight == "on":
                print("\nYou turn off the flashlight.")
                self.flashlight = "off"
            elif self.flashlight == "off":
                print("\nThe flashlight is already", self.flashlight)
        else:
            error(1)

    def use_paper( self, action ):
        print(note_room_paper)

    def add_to_inventory( self, item ):
        if item not in self.inventory:
            self.inventory.append( item )
            print(f"\nYou put the {item} in your bag.")
