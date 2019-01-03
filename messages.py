from textwrap import dedent

welcome_text = open("plantgame_welcome.txt", 'r')

#>----room_attr.py

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

no_paper = "There is no paper here."

flashlight_inventory_message = dedent(
"""
You take the flashlight and test it.
The battery is full. It works.
The plants do not react to the light."""
)

flashlight_inventory_taken = "\nThere is an empty flashlight mount on the wall."

no_flashlight = "\nThere is no flashlight here."

heat_room_help = dedent(
"""
You turned the dial.
Heat blasts through the building.
The plants love it!
New branches shoot across the wall."""
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


#>----building.py messages
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

#>----actions.py messages
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

#>----player.py messages
turn_on_flashlight_text = dedent("""
You turn on the flashlight.
You can see the room now.
The plants are not affected by the light.
""")
