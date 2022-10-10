import json

j_file=open("./static/json/info.json","r")
info=json.load(j_file)
print(info["CHANNEL_ACCESS_TOKEN"])