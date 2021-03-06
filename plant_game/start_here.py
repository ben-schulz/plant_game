import building as b
import plant as p
import player
import play
import room_attr as r

#This is a Plant Game!
#author: Lynn Chiu
#Last update: 2019/1/5

#A text-based escape room game

#generate room objects from room_attr file and building module
map = r.Map()
rooms_dict = {}
for values in map.room_attr_dict.values():
    room_name = values["name"]
    rooms_dict.update({room_name: b.Room(values)})

#generate game with plant and player objects
game = play.Play(p.Plant(), player.Player(), rooms_dict)

#start with "note_room" as starting room
game.start('note_room')
