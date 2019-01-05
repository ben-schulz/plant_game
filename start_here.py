import building as b
import plant as p
import player as player
import play as play
import room_attr as r

#generate rooms from room_attr file and building module
map = r.Map()
rooms_dict = {}
for key, values in map.room_attr_dict.items():
    room_name = values["name"]
    room_attr = key
    rooms_dict.update({room_name: b.Room(map.room_attr_dict[room_attr])})

#generate game
game = play.Play(p.Plant(), player.Player(), rooms_dict)
game.start('note_room')
