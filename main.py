from createdb import createdb
from printxl import printxl
from flask import Flask, render_template, request
import sqlite3
import datetime


today = datetime.date.today()#今日の日付
db = "students"
# DBを作成する（既に作成されていたらこのDBに接続する
dbname = f"./database/{db}.db"
conn = sqlite3.connect(dbname)
#SQLiteを操作するためのカーソル,コントローラー
cur = conn.cursor()
#データベース内の表示
info = []
records = cur.execute("SELECT * FROM students")
for record in records:
    info.append(list(record))
#print(info)
# コミットしないと登録が反映されない

conn.commit()

key = ["学籍番号", "名前", "出席", "遅刻", "早退"]
stdlist = [dict(zip(key,item)) for item in info]#keyとinfoをまとめて辞書型にする


app = Flask(__name__)
#トップページ
@app.route("/", methods=["GET","POST"])
def top():
    return render_template("/displaydb.html", stdlist = stdlist, today = today)#stdlistはdb内の情報が辞書型で入っている変数



printxl(db)
if __name__ == "__main__":
    app.run(debug=True)






