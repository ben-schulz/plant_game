import building as b
import plant as p
import player as player
import play as play
import room_attr as r

#generate plant
plant = p.Plant()

#generate player
player = player.Player()

#generate rooms from room_attr file and building module
rooms_dict = {}
for key, values in r.room_attr_dict.items():
    room_name = values["name"]
    room_attr = key
    rooms_dict.update({room_name: b.Room(r.room_attr_dict[room_attr])})

#generate game
game = play.Play(plant, player, rooms_dict)
game.start('note_room')
