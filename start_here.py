from sys import exit
from textwrap import dedent
import actions as a
import building
import plant as p
import ending
import player
import messages as m

class Play():

    def __init__( self ):
        pass

    def enter( self, next_room ):
        flag = False

        while flag == False:
            current_room = building.rooms[ next_room ]
            next_room = a.room_decisions( current_room )

            #check whether game over
            plants_win = p.plant.check_over_growth()
            end_room = ending.check_room( next_room )
            if end_room or plants_win :
                flag = True
            else:
                flag = False

        ending.game_over( next_room, plants_win )

    def start( self, starting_room ):
        #display game intro text
        for line in m.welcome_text:
            print(line.strip())

        #call room
        current_room = building.rooms[starting_room]
        #do actions in room and call next room
        next_room = a.room_decisions( current_room )
        self.enter( next_room )

game = Play()
game.start('note_room')
