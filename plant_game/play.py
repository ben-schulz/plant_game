from sys import exit
from textwrap import dedent

#>--- texts used in this file
welcome_text = dedent("""
    You wake up in a room with a large window.
    Outside, you see a lush forest all the way to the horizon.
    It's beautiful and calm out there.

    But back in the room...slimey, thick dark vines cover the walls and floors.
    Astonished, you see that they're growing at a rapid speed!
    Slithering across the wall. Like snakes.
    The roots ripple as they cover the floor.""")

plants_win = dedent(
"""
Game over.
The plants have overgrown the building.
You are stuck in here forever.
""")

exit_text = dedent(
"""
Game over, you win!
You got out before the plants overwhelmed the room!
"""
)

death_text = dedent(
"""
You fall into a pit full of worms.
As you flail about.
You slowly suffucate.

Game over.
""")

#>--- main functions


class Play():

    def __init__( self, plant, player, rooms_dict ):
        self.plant = plant
        self.player = player
        self.rooms_dict = rooms_dict

    def game_over( self, next_room, plants_win ):
        plants_win = self.plant.check_over_growth()

        if plants_win:
            print(plants_win)
        if next_room == "exit":
            print(exit_text)
        elif next_room == "death":
            print(death_text)

    def check_game_over( self, next_room ):
        plants_win = self.plant.check_over_growth()

        def check_room():
            if next_room == "death":
                return True
            elif next_room == "exit":
                return True
            else:
                return False

        if check_room() or plants_win:
            return True
        else:
            return False

    def enter( self, next_room ):
        flag = False

        while flag == False:
            current_room = self.rooms_dict[ next_room ]
            next_room = current_room.room_decisions( self.plant, self.player )

            #check whether game over
            flag = self.check_game_over( next_room )

        self.game_over( next_room, plants_win )

    def start( self, starting_room ):
        print( welcome_text )
        current_room = self.rooms_dict[ starting_room ]
        next_room = current_room.room_decisions( self.plant, self.player )
        self.enter( next_room )
