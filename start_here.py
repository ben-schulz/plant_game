from sys import exit
from textwrap import dedent

import actions as a
import building as b
import plant as p
import messages as m


def game_over( next_room, plants_win ):
    if plants_win:
        print(m.plants_win)
    if next_room == "exit":
        print(m.exit_text)
    if next_room == "death":
        print(m.death_text)

class Play():

    def __init__( self ):
        pass

    def enter( self, next_room ):
        flag = False

        while flag == False:
            current_room = b.rooms[ next_room ]
            next_room = a.room_decisions( current_room )

            #check whether game over
            plants_win = p.plant.check_over_growth()
            end_room = b.check_room( next_room )
            if end_room or plants_win :
                flag = True
            else:
                flag = False

        game_over( next_room, plants_win )

    def start( self, starting_room ):
        print(m.welcome_text)
        current_room = b.rooms[starting_room]
        next_room = a.room_decisions( current_room )
        self.enter( next_room )

game = Play()
game.start('note_room')
