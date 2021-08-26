import json

myjsonfile = open('database.json', 'r')

jsondata = myjsonfile.read()
myjsonfile.close()

# parse
game = json.loads(jsondata)

# print(game)
# print(type(game))==> gives dict
# print(str( game["1198490"]))
# print(type(game["1198490"]))

for steam_appid in game.values():
     print(steam_appid)
print("Name:"+steam_appid["name"])

'''for item in steam_appid:
    game_name=item['name']
    age=item['required_age']
    new_list=steam_appid(game_name=name,age=required_age)
    print(new_list)'''



# for key in steam_appid.values():
#     print(key['name'])
# for game_name in key['name']:
#     print(game_name['name'])
# #to get a list we ith all the game names:
# for item in game['name']:
#     print(item)

