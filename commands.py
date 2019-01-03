"""captures possible user inputs"""

#>----doors and windows
door_actions = { #N, E, S, W
    "north": ["north", "north door", "open north door", "open north", "door north", "enter north door"],
    "east": ["east", "east door", "open east door", "open east", "door east", "enter east door"],
    "south": ["south", "south door", "open south door", "open south", "door south", "go to south door", "enter south door"],
    "west": ["west", "west door", "open west door", "open west", "door west", "go to west door", "enter west door"]
}

window_on_actions = ["window", "windows","shutters", "shutter", "open windows",  "open shutters", "open window", "open shutter", "window open", "windows open"]

window_close_actions = ["window", "windows","shutters", "shutter", "close windows","close shutters", "close window", "close shutter", "window close", "shutter close", "shutters close"]

window_actions = window_on_actions + window_close_actions

#>----room feature
dial_actions = ["dial", "turn dial", "open dial", "use dial", "dial left", "dial right", "dial clockwise", "dial counterclockwise"]

faucet_actions = ["faucet", "turn faucet", "use faucet", "twist faucet"]

plant_actions = ["plant", "touch plant", "pull plant", "move plant"]


#>----inventory
flashlight_on_actions = ["flashlight", "take flashlight", "use flashlight", "get flashlight", "turn on flashlight", "flashlight on", "on flashlight", "open flashlight"]

flashlight_off_actions = ["turn off flashlight", "put away flashlight", "flashlight off", "off flashlight", "close flashlight", "not use flashlight"]

flashlight_actions = flashlight_on_actions + flashlight_off_actions

paper_actions = ["paper", "read", "read paper", "pick up paper", "pick up", "get paper"]

inventory_actions = {
    "flashlight": flashlight_actions,
    "paper": paper_actions,
}
