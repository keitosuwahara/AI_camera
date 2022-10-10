import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

j_file=open("./static/json/info.json","r")
info=json.load(j_file)

CHANNEL_ACCESS_TOKEN=info["CHANNEL_ACCESS_TOKEN"]
line_bot_api=LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    