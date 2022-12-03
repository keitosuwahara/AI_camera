import sqlite3
from createdb import studentdb , admindb
import datetime
from flask import Flask, render_template, request

#作成した出欠席表をwebに表示とDBの更新をするプログラムです

studentdb()#学生データベースを作る
admindb()#管理者用データベースを作る

# DBを作成する（既に作成されていたらこのDBに接続する
dbname ="./database/students.db"
conn = sqlite3.connect(dbname)
#SQLiteを操作するためのカーソル,コントローラー
cur = conn.cursor()
#update用のSQL
update_sql = 'UPDATE students SET 名前="志村燿平" WHERE 学籍番号=186758'
# データ更新
cur.execute(update_sql)
cur.execute('UPDATE students SET 学籍番号= 186758 WHERE 名前="志村燿平"')
cur.execute('UPDATE students SET 出席=1 WHERE 名前="志村燿平"')

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

#dbの人数をdb.txtに転記する処理
with open("./database/population.txt","w",encoding="utf-8")as datafile:
    datafile.write(str(len(info)))




app = Flask(__name__)
studentnumlist=[]
namelist=[]
attendancelist=[]
#トップページ
@app.route("/", methods=["GET","POST"])
def top():
#5文字以上の数字のみ抜き出すつまり学籍番号
    for users in info:
        for student in list(users):
            if str(student).isdigit() == True and len(str(student)) > 5:
                studentnumlist.append(student)
#日本語とカタカナ、アルファベットの文字列を抜き出す、つまり名前
    for users in info:
        for student in list(users):
            if str(student).isalpha():
                namelist.append(student)
#2文字以下の数字のみ抜き出す、つまり出欠席
    for users in info:
        for student in list(users):
            if str(student).isdigit() == True and len(str(student)) < 2:
                attendancelist.append(student)
    return render_template("/displaydb.html", studentnumlist = studentnumlist, namelist = namelist, attendancelist = attendancelist)

#こんなことしなくてもenumerate()つかえばできたね..

if __name__ == "__main__":
    app.run(debug=True)













