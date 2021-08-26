import json

myjsonfile = open('database.json')

jsondata = myjsonfile.read()
myjsonfile.close()
#parse
game=json.loads(jsondata)

print(game)


