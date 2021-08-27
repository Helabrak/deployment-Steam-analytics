import json

myjsonfile = open('database.json', 'r')

jsondata = myjsonfile.read()
myjsonfile.close()

# parse
game = json.loads(jsondata)

# print(game)#returns all data is mess (raw_data)
# print(type(game))#to get the type of data (in this case dict)
#print(str( game["1198490"])) #prints one instance (all the keys and values of this index)
#print(type(game["1198490"]))#prints the type of this instance

#parsing game names (to get a list we ith all the game names):
for steam_appid in game.values():
     #print(steam_appid) #returns all the dictionnaries in the data
     game_name="Name:" + steam_appid["name"]
     game_description= "Description:" + steam_appid["short_description"]
     print(game_name),#game_description)