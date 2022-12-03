import sqlite3
from createdb import studentdb , admindb
import datetime
from flask import Flask, render_template, request

today = datetime.date.today()#今日の日付

#作成した出欠席表をwebに表示とDBの更新をするプログラムです

studentdb()#学生データベースを作る
admindb()#管理者用データベースを作る

# DBを作成する（既に作成されていたらこのDBに接続する
dbname ="./database/students.db"
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
#print(info)#[[186758, '志村燿平', 1], [190721, '岩橋大地', 1], [200284, '桃崎奏斗', 1], [210103, '諏訪原慶斗', 1], [435755, '高田悠', 0], [557855, '黒野怜奈', 1], [846556, 'トゴーフーバダムツェレン', 1]]
#print(len(info))#データベースの人数を出力

key = ["学籍番号", "名前", "出席", "遅刻", "早退"]
stdlist = [dict(zip(key,item)) for item in info]#keyとinfoをまとめて辞書型にする


app = Flask(__name__)

#トップページ
@app.route("/", methods=["GET","POST"])
def top():

    return render_template("/displaydb.html", stdlist = stdlist, today = today)#stdlistはdb内の情報が辞書型で入っている変数

#こんなことしなくてもenumerate()つかえばできたね..

if __name__ == "__main__":
    app.run(debug=True)













