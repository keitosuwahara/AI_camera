"https://qiita.com/sugiyama404/items/7691d7ff6a5b8c24eddf"
import json



j_file_path="./static/json/info.json"
j_file=open(j_file_path,"r")
info=json.load(j_file)

CHANNEL_ACCESS_TOKEN=info["someone"]
print(CHANNEL_ACCESS_TOKEN["CHANNEL_ACCESS_TOKEN"])


