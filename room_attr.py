from textwrap import dedent

dial_actions = ["dial", "turn dial", "open dial", "use dial", "dial left", "dial right", "dial clockwise", "dial counterclockwise"]

faucet_actions = ["faucet", "turn faucet", "use faucet", "twist faucet"]

paper_actions = ["paper", "read", "read paper", "pick up paper", "pick up", "get paper"]

flashlight_actions = ["flashlight", "take flashlight", "get flashlight", "pick up flashlight"]


#>---- texts used in this file go here
symbiont_room_message = dedent("""
Mud sloshes around the room.
Teeming with insects and slimy with fungi...
You see a sign: "GMO SUPER-SYMBIONTS"
This is the source of the plants' crazy growth!
You see that the mud is oozing in from the west door.
""")

water_room_message = dedent("""
On the wall of this room, you see an open faucet.
The room is flooded with water.
Root systems cover the floor.
""")

water_room_harm_plant =  dedent(
"""
You tighten the faucet.
The pools of water drained off.
"""
)

water_room_help_plant = dedent(
"""
Open faucet.
The roots glisten with moisture.
"""
)

water_room_harm_plant_room = "\nPlants rustle around the closed faucet, as if displeased."

water_room_help_plant_room = "\nThere is a running faucet."

note_room_message = dedent("""
There is a piece of paper on the floor.
""")

note_room_inventory_taken = "An entanglement of roots crawl over the floor."

note_room_paper = dedent(f"""
You flip the piece of paper around.
Scrawled in bad handwriting:

    GET OUT NOW!!!
    The experiment... the GMO symbionts are driving the growth.
    The plants are now everywhere.
    They're growing fast, sealing off doors, covering the building...
    Run! Get out of the building before it's too late!""")

no_paper = "There is no paper here."


flash_light_message = dedent("""
        There is a flashlight on the wall.
        """)

flashlight_inventory_message = dedent(
"""
You take the flashlight and test it.
The battery is full. It works.
The plants do not react to the light."""
)

flashlight_inventory_taken = "\nThere is an empty flashlight mount on the wall."

no_flashlight = "\nThere is no flashlight here."

heat_room_message= dedent("""
This seems to be the climate control room.
There is a dial on the wall.
It looks like a thermostat.
""")

heat_room_help = dedent(
"""
You turned the dial.
Heat blasts through the building.
The plants love it!
"""
)

heat_room_harm = dedent(
"""
You turn the dial the other way.
Now the air conditioning is on.
The plants hate the cold.
"""
)

heat_room_harm_room = "\nThe air conditioner is on."

heat_room_help_room = "\nThe leaves spread wide under the radiator heat."

room_with_exit_message = dedent("""
You feel a gentle breeze.
""")

#>-- main file

class Map( object ):
    room_attr_dict = {

        "symbiont_room_attr" : {
            "name": "symbiont_room",
            "window": "closed",
            "doors": {"east": "water_room", "west": "death",},
            "action": "None",
            "inventory_action": "None",

            "message": symbiont_room_message,
        },

        "water_room_attr" : {
            "name": "water_room",
            "window": "closed",
            "doors": {"south": "west_note_room", "west": "symbiont_room", "north": "room_with_exit"},
            "inventory_action": "None",
        #room feature
            "action": faucet_actions,

            "feature": "on",
            "harm_plant_message": water_room_harm_plant,
            "help_plant_message": water_room_help_plant,
            "harm_plant_room_message": water_room_harm_plant_room,
            "help_plant_room_message": water_room_help_plant_room,

            "message": water_room_message,
        },

        "west_note_room_attr" : {
            "name": "west_note_room",
            "window": "closed",
            "doors": {"east": "note_room", "north": "water_room"},
            "action": "None",
            "inventory_action": "None",
        },

        "note_room_attr" : {
            "name": "note_room",
            "window": "open",
            "doors": {"east": "east_note_room", "west": "west_note_room"},
            "action": "None",

        #inventory
            "inventory_action": paper_actions,
            "inventory_item": "paper",
            "inventory_feature": "exist",
            "inventory_message": note_room_paper,
            "inventory_taken_message": note_room_inventory_taken,
            "no_item_message": no_paper,

            "message": note_room_message,
        },

        "east_note_room_attr" : {
            "name": "east_note_room",
            "window": "closed",
            "doors": {"west": "note_room", "north": "heat_room", "south": "flashlight_room"},
            "action": "None",
            "inventory_action": "None",

        },

        "flashlight_room_attr" : {
            "name": "flashlight_room",
            "window": "closed",
            "doors": {"north": "east_note_room"},
            "action": "None",
        #inventory
            "inventory_item": "flashlight",
            "inventory_action": flashlight_actions,
            "inventory_feature": "exist",
            "inventory_message": flashlight_inventory_message,
            "inventory_taken_message": flashlight_inventory_taken,
            "no_item_message": no_flashlight,

            "message": flash_light_message,

        },

        "heat_room_attr" : {
            "name": "heat_room",
            "window": "closed",
            "doors": {"south": "east_note_room",},
            "inventory_action": "None",
        #room feature
            "action": dial_actions,
            "feature": "off",
            "help_plant_message": heat_room_help,
            "harm_plant_message": heat_room_harm,
            "harm_plant_room_message": heat_room_harm_room,
            "help_plant_room_message": heat_room_help_room,

            "message": heat_room_message,
        },

        "room_with_exit_attr" : {
            "name": "room_with_exit",
            "window": "closed",
            "doors": {"north": "exit", "south": "water_room",},
            "action": "None",
            "inventory_action": "None",

            "message": room_with_exit_message,
        },
    }
