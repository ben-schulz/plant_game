from textwrap import dedent
import commands as c
import messages as m


symbiont_room_attr = {
    "name": "symbiont_room",
    "window": "closed",
    "message": m.symbiont_room_message,
    "doors": {"east": "water_room", "west": "death",},
    "action": "None",
    "inventory_action": "None",
}

water_room_attr = {
    "name": "water_room",
    "window": "closed",
    "message": m.water_room_message,
    "doors": {"south": "west_note_room", "west": "symbiont_room", "north": "room_with_exit"},
    "inventory_action": "None",
#room feature
    "action": c.faucet_actions,
    "feature": True,
    "harm_plant_message": m.water_room_harm_plant,
    "help_plant_message": m.water_room_help_plant,
    "harm_plant_room_message": m.water_room_harm_plant_room,
    "help_plant_room_message": m.water_room_help_plant_room,
}

west_note_room_attr = {
    "name": "west_note_room",
    "window": "closed",
    "doors": {"east": "note_room", "north": "water_room"},
    "action": "None",
    "inventory_action": "None",

}

note_room_attr = {
    "name": "note_room",
    "window": "open",
    "message": m.note_room_message,
    "doors": {"east": "east_note_room", "west": "west_note_room"},
    "action": "None",
#inventory
    "inventory_item": "paper",
    "inventory_action": c.paper_actions,
    "inventory_feature": True,
    "inventory_message": open("plantgame_paper.txt", 'r').read().rstrip(),
    "inventory_taken_message": m.note_room_inventory_taken,
    "no_item_message": m.no_paper,

}

east_note_room_attr = {
    "name": "east_note_room",
    "window": "closed",
    "doors": {"west": "note_room", "north": "heat_room", "south": "flashlight_room"},
    "action": "None",
    "inventory_action": "None",

}

flashlight_room_attr = {
    "name": "flashlight_room",
    "window": "closed",
    "message": dedent("""
    There is a flashlight on the wall.
    """),
    "doors": {"north": "east_note_room"},
    "action": "None",
#inventory
    "inventory_item": "flashlight",
    "inventory_action": c.flashlight_actions,
    "inventory_feature": True,
    "inventory_message": m.flashlight_inventory_message,
    "inventory_taken_message": m.flashlight_inventory_taken,
    "no_item_message": m.no_flashlight,

}

heat_room_attr = {
    "name": "heat_room",
    "window": "closed",
    "message": dedent("""
    This seems to be the climate control room.
    There is a dial on the wall.
    It looks like a thermostat.
    """),
    "doors": {"south": "east_note_room"},
    "inventory_action": "None",
#room feature
    "action": c.dial_actions,
    "feature": False,
    "help_plant_message": m.heat_room_help,
    "harm_plant_message": m.heat_room_harm,
    "harm_plant_room_message": m.heat_room_harm_room,
    "help_plant_room_message": m.heat_room_help_room,
}

room_with_exit_attr = {
    "name": "room_with_exit",
    "window": "closed",
    "message": dedent("""
    You feel a gentle breeze.
    """),
    "doors": {"north": "exit", "south": "water_room",},
    "action": "None",
    "inventory_action": "None",
}
